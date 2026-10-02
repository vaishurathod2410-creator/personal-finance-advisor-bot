"""
Savings Goal Tracker & What-If Scenario Analysis Module
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
from translations import get_text

def render_savings_tracker(lang: str):
    """Render the Savings Goal Tracker & What-If Analysis view."""
    profile = st.session_state.user_profile
    income = profile.get("income", 50000.0)
    expenses = profile.get("expenses", 30000.0)
    surplus = max(0.0, income - expenses)

    st.markdown(f"## {get_text('savings_title', lang)}")
    st.caption(get_text("savings_desc", lang))

    # Goal Tracker Inputs
    with st.container():
        st.markdown("<div class='fb-card'>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            goal_name = st.text_input(get_text("goal_name", lang), value=profile.get("goal", "Build Emergency Fund"))
            target_amount = st.number_input(get_text("target_amount", lang), min_value=1000.0, value=150000.0, step=5000.0)
        with col2:
            current_saved = st.number_input(get_text("current_saved", lang), min_value=0.0, value=30000.0, step=2000.0)
            target_months = st.number_input(get_text("target_months", lang), min_value=1, max_value=120, value=12, step=1)
        st.markdown("</div>", unsafe_allow_html=True)

    # Calculation logic
    remaining_amount = max(0.0, target_amount - current_saved)
    monthly_req = remaining_amount / target_months if target_months > 0 else remaining_amount
    progress_pct = min(100.0, (current_saved / target_amount * 100.0) if target_amount > 0 else 100.0)

    # Progress Bar Display
    st.markdown(f"### 📊 Progress for: **{goal_name}**")
    st.progress(progress_pct / 100.0)
    
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(get_text("monthly_req", lang), f"₹{monthly_req:,.0f}/mo")
    with col_m2:
        st.metric(get_text("available_surplus", lang), f"₹{surplus:,.0f}/mo")
    with col_m3:
        st.metric("Progress Saved", f"{progress_pct:.1f}%", f"₹{current_saved:,.0f} / ₹{target_amount:,.0f}")

    # Status Advice Box
    if monthly_req <= surplus:
        st.success(f"{get_text('goal_achievable', lang)} (You have ₹{surplus - monthly_req:,.0f} remaining surplus every month!)")
    elif monthly_req <= surplus * 1.25:
        st.warning(get_text("goal_tight", lang))
    else:
        st.error(get_text("goal_overbudget", lang))

    # What-If Analysis Section
    st.markdown("---")
    st.markdown(f"### 🔮 {get_text('what_if_title', lang)}")
    st.caption(get_text("what_if_desc", lang))

    extra_saving = st.slider(
        get_text("extra_save_label", lang),
        min_value=0,
        max_value=25000,
        value=3000,
        step=500
    )

    # Calculate What-If comparison
    std_monthly_save = surplus
    new_monthly_save = surplus + extra_saving

    # Time to reach goal under both scenarios
    std_months_needed = remaining_amount / std_monthly_save if std_monthly_save > 0 else 999
    new_months_needed = remaining_amount / new_monthly_save if new_monthly_save > 0 else 999
    
    months_saved = max(0, std_months_needed - new_months_needed)

    # Metric Cards for What-If
    w_col1, w_col2 = st.columns(2)
    with w_col1:
        st.markdown(
            f"""
            <div class="fb-metric-card blue">
                <div class="fb-metric-title">⚡ Time Saved</div>
                <div class="fb-metric-value">{new_months_needed:.1f} Months</div>
                <div style="font-size:0.85rem; color:#2563EB;">(Reaches goal <b>{months_saved:.1f} months faster!</b>)</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Investment Growth Projection (8% annual return compounded monthly)
    annual_rate = 0.08
    r_monthly = annual_rate / 12
    months_proj = min(60, max(12, int(std_months_needed)))
    
    months_axis = list(range(1, months_proj + 1))
    std_trajectory = []
    extra_trajectory = []

    std_val = current_saved
    extra_val = current_saved

    for m in months_axis:
        std_val = (std_val + std_monthly_save) * (1 + r_monthly)
        extra_val = (extra_val + new_monthly_save) * (1 + r_monthly)
        std_trajectory.append(round(std_val, 2))
        extra_trajectory.append(round(extra_val, 2))

    with w_col2:
        wealth_diff = extra_trajectory[-1] - std_trajectory[-1]
        st.markdown(
            f"""
            <div class="fb-metric-card">
                <div class="fb-metric-title">📈 Wealth Created @ 8% p.a.</div>
                <div class="fb-metric-value">₹{extra_trajectory[-1]:,.0f}</div>
                <div style="font-size:0.85rem; color:#059669;">(+₹{wealth_diff:,.0f} extra wealth in {months_proj} mos)</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Plotly Line Chart for Trajectory Comparison
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(
        x=months_axis, y=std_trajectory,
        mode='lines',
        name='Current Monthly Surplus',
        line=dict(color='#94A3B8', width=3, dash='dash')
    ))
    fig_line.add_trace(go.Scatter(
        x=months_axis, y=extra_trajectory,
        mode='lines',
        name=f'With Extra ₹{extra_saving:,.0f}/month',
        line=dict(color='#10B981', width=4)
    ))
    fig_line.add_hline(
        y=target_amount,
        line_dash="dot",
        line_color="#EF4444",
        annotation_text=f"Target Goal: ₹{target_amount:,.0f}",
        annotation_position="bottom right"
    )

    fig_line.update_layout(
        title="Savings Trajectory & Goal Target Projection",
        xaxis_title="Months",
        yaxis_title="Total Savings Accumulated (₹)",
        margin=dict(t=40, b=20, l=10, r=10),
        height=350,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    st.plotly_chart(fig_line, use_container_width=True)
