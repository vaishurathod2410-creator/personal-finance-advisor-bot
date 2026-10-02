"""
Personalized Budget Maker Module using the 50/30/20 Rule and Plotly visuals.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from translations import get_text
from modules.user_profile import calculate_health_score

def render_budget_maker(lang: str):
    """Render the complete Budget Maker view."""
    profile = st.session_state.user_profile
    income = profile.get("income", 50000.0)
    expenses = profile.get("expenses", 30000.0)

    st.markdown(f"## {get_text('budget_title', lang)}")
    st.caption(get_text("budget_desc", lang))

    # Health score card top view
    health_data = calculate_health_score(income, expenses)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.markdown(
            f"""
            <div class="fb-card" style="text-align:center;">
                <div style="font-size:0.9rem; color:#64748B; font-weight:600;">{get_text('monthly_income', lang)}</div>
                <div style="font-size:1.8rem; font-weight:800; color:#2563EB;">₹{income:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"""
            <div class="fb-card" style="text-align:center;">
                <div style="font-size:0.9rem; color:#64748B; font-weight:600;">{get_text('monthly_expenses', lang)}</div>
                <div style="font-size:1.8rem; font-weight:800; color:#EF4444;">₹{expenses:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            f"""
            <div class="fb-card" style="text-align:center;">
                <div style="font-size:0.9rem; color:#64748B; font-weight:600;">{get_text('health_score_title', lang)}</div>
                <div style="font-size:1.8rem; font-weight:800; color:{health_data['color_code']};">{health_data['score']}/100</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 50/30/20 Recommended Breakdown
    rec_needs = income * 0.50
    rec_wants = income * 0.30
    rec_savings = income * 0.20

    st.markdown(f"### 🎯 {get_text('rule_50_30_20', lang)}")
    
    c_needs, c_wants, c_sav = st.columns(3)
    with c_needs:
        st.info(f"**{get_text('needs_label', lang)}**\n\n### ₹{rec_needs:,.0f}")
    with c_wants:
        st.warning(f"**{get_text('wants_label', lang)}**\n\n### ₹{rec_wants:,.0f}")
    with c_sav:
        st.success(f"**{get_text('savings_invest_label', lang)}**\n\n### ₹{rec_savings:,.0f}")

    st.markdown("---")
    st.markdown(f"### 🛒 {get_text('category_breakdown', lang)}")
    st.caption("Customize your current breakdown to compare against recommended limits:")

    # Detailed Expense Breakdown Form
    if "budget_categories" not in st.session_state:
        st.session_state.budget_categories = {
            "rent": expenses * 0.35,
            "food": expenses * 0.25,
            "bills": expenses * 0.15,
            "transport": expenses * 0.10,
            "entertainment": expenses * 0.10,
            "misc": expenses * 0.05
        }

    b_cats = st.session_state.budget_categories

    col_cat1, col_cat2 = st.columns(2)
    with col_cat1:
        rent = st.number_input(get_text("rent_housing", lang), min_value=0.0, value=float(b_cats["rent"]), step=500.0)
        food = st.number_input(get_text("food_groceries", lang), min_value=0.0, value=float(b_cats["food"]), step=500.0)
        bills = st.number_input(get_text("utilities_bills", lang), min_value=0.0, value=float(b_cats["bills"]), step=500.0)

    with col_cat2:
        transport = st.number_input(get_text("transport", lang), min_value=0.0, value=float(b_cats["transport"]), step=500.0)
        entertainment = st.number_input(get_text("entertainment", lang), min_value=0.0, value=float(b_cats["entertainment"]), step=500.0)
        misc = st.number_input(get_text("misc", lang), min_value=0.0, value=float(b_cats["misc"]), step=500.0)

    total_custom_expenses = rent + food + bills + transport + entertainment + misc
    actual_needs = rent + food + bills + transport
    actual_wants = entertainment + misc
    actual_savings = max(0.0, income - total_custom_expenses)

    # Save back to profile if changed
    if total_custom_expenses != expenses:
        st.session_state.user_profile["expenses"] = total_custom_expenses
        st.session_state.budget_categories = {
            "rent": rent, "food": food, "bills": bills,
            "transport": transport, "entertainment": entertainment, "misc": misc
        }

    # Charts Section
    st.markdown("---")
    st.markdown(f"### 📈 {get_text('actual_vs_recommended', lang)}")

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        # Donut Chart for Expense Category Breakdown
        labels = [
            get_text("rent_housing", lang),
            get_text("food_groceries", lang),
            get_text("utilities_bills", lang),
            get_text("transport", lang),
            get_text("entertainment", lang),
            get_text("misc", lang)
        ]
        values = [rent, food, bills, transport, entertainment, misc]

        fig_donut = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=.45,
            marker_colors=['#2563EB', '#3B82F6', '#60A5FA', '#F59E0B', '#EF4444', '#94A3B8']
        )])
        fig_donut.update_layout(
            title_text="Your Expense Breakdown",
            margin=dict(t=40, b=10, l=10, r=10),
            height=320,
            showlegend=True
        )
        st.plotly_chart(fig_donut, use_container_width=True)

    with col_chart2:
        # Bar Chart comparing Recommended 50/30/20 vs Actual
        fig_bar = go.Figure(data=[
            go.Bar(name='Recommended (50/30/20)', x=['Needs', 'Wants', 'Savings'], y=[rec_needs, rec_wants, rec_savings], marker_color='#93C5FD'),
            go.Bar(name='Your Actual', x=['Needs', 'Wants', 'Savings'], y=[actual_needs, actual_wants, actual_savings], marker_color='#2563EB')
        ])
        fig_bar.update_layout(
            barmode='group',
            title_text="Recommended vs Actual Budget",
            margin=dict(t=40, b=10, l=10, r=10),
            height=320,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # Smart Budget Advice Card
    st.markdown(f"### 💡 {get_text('budget_analysis', lang)}")
    advice_list = []

    if actual_needs > rec_needs:
        diff = actual_needs - rec_needs
        advice_list.append(f"⚠️ **Needs Alert:** Your basic needs (₹{actual_needs:,.0f}) exceed the 50% limit by ₹{diff:,.0f}. Try optimizing rent or utility bills.")
    else:
        advice_list.append("✅ **Needs Check:** Great! Your basic living expenses are well within the 50% recommended limit.")

    if actual_wants > rec_wants:
        diff_w = actual_wants - rec_wants
        advice_list.append(f"⚠️ **Wants Alert:** You are spending ₹{diff_w:,.0f} more than recommended on lifestyle/entertainment. Cutting back slightly will boost your savings.")
    else:
        advice_list.append("✅ **Wants Check:** Your discretionary spending is within control!")

    if actual_savings < rec_savings:
        diff_s = rec_savings - actual_savings
        advice_list.append(f"🚨 **Savings Alert:** You are saving ₹{actual_savings:,.0f}/month. Try to save an extra ₹{diff_s:,.0f}/month to reach the recommended 20% mark.")
    else:
        advice_list.append("🌟 **Savings Champion:** You are saving 20% or more of your income! Keep investing this regularly.")

    for adv in advice_list:
        st.markdown(f"<div class='fb-metric-card blue'>{adv}</div>", unsafe_allow_html=True)
