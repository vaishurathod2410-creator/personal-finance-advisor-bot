"""
EMI Calculator, Loan Recommendation System, and Bank Disbursal Safety Guidelines.
"""

import streamlit as st
import plotly.graph_objects as go
from translations import get_text
from config import LOAN_TYPES

def calculate_emi(principal: float, annual_rate: float, tenure_years: float) -> tuple[float, float, float]:
    """Calculate Monthly EMI, Total Interest, and Total Payment."""
    if principal <= 0 or annual_rate <= 0 or tenure_years <= 0:
        return 0.0, 0.0, 0.0

    monthly_rate = annual_rate / (12 * 100)
    total_months = tenure_years * 12

    try:
        emi = principal * monthly_rate * ((1 + monthly_rate) ** total_months) / (((1 + monthly_rate) ** total_months) - 1)
        total_payment = emi * total_months
        total_interest = total_payment - principal
        return round(emi, 2), round(total_interest, 2), round(total_payment, 2)
    except Exception:
        return 0.0, 0.0, 0.0

def render_emi_loan(lang: str):
    """Render the EMI Calculator & Safe Loan Recommendation interface."""
    profile = st.session_state.user_profile
    income = profile.get("income", 50000.0)
    expenses = profile.get("expenses", 30000.0)
    surplus = max(0.0, income - expenses)

    st.markdown(f"## {get_text('emi_title', lang)}")

    tab1, tab2 = st.tabs([
        f"🧮 {get_text('emi_calculator', lang)}",
        f"🏦 {get_text('loan_recommend_title', lang)}"
    ])

    with tab1:
        st.markdown("<div class='fb-card'>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            loan_amt = st.number_input(get_text("loan_amount_label", lang), min_value=10000.0, value=200000.0, step=10000.0)
        with c2:
            interest_rate = st.number_input(get_text("interest_rate_label", lang), min_value=1.0, max_value=36.0, value=11.5, step=0.25)
        with c3:
            tenure_yr = st.number_input(get_text("tenure_label", lang), min_value=0.5, max_value=30.0, value=3.0, step=0.5)
        st.markdown("</div>", unsafe_allow_html=True)

        emi, interest, total_pay = calculate_emi(loan_amt, interest_rate, tenure_yr)

        # EMI Metrics Display
        col_e1, col_e2, col_e3 = st.columns(3)
        with col_e1:
            st.metric(get_text("monthly_emi_result", lang), f"₹{emi:,.0f}/mo")
        with col_e2:
            st.metric(get_text("total_interest_result", lang), f"₹{interest:,.0f}")
        with col_e3:
            st.metric(get_text("total_payment_result", lang), f"₹{total_pay:,.0f}")

        # Affordability Ratio (EMI / Income)
        emi_income_ratio = (emi / income * 100) if income > 0 else 100
        st.markdown(f"#### ⚖️ {get_text('emi_affordability', lang)} ({emi_income_ratio:.1f}% of income)")

        if emi_income_ratio <= 35:
            st.success(get_text("safe_emi", lang))
        elif emi_income_ratio <= 50:
            st.warning(get_text("moderate_emi", lang))
        else:
            st.error(get_text("risky_emi", lang))

        # Pie chart for Principal vs Interest
        fig_pie = go.Figure(data=[go.Pie(
            labels=['Principal Loan Amount', 'Total Interest Payable'],
            values=[loan_amt, interest],
            hole=.4,
            marker_colors=['#2563EB', '#F59E0B']
        )])
        fig_pie.update_layout(
            title_text="Loan Principal vs Interest Ratio",
            margin=dict(t=40, b=10, l=10, r=10),
            height=280
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with tab2:
        st.markdown(f"### {get_text('loan_recommend_title', lang)}")
        st.caption("Custom loan eligibility and best choices tailored to your salary.")

        purpose_options = {
            get_text("goal_bike", lang): "bike",
            get_text("goal_gadget", lang): "phone",
            get_text("goal_home", lang): "house",
            get_text("goal_education", lang): "education",
            "Personal / Emergency": "personal"
        }

        selected_purpose_name = st.selectbox(get_text("loan_purpose_label", lang), options=list(purpose_options.keys()))
        loan_key = purpose_options[selected_purpose_name]
        loan_meta = LOAN_TYPES[loan_key]

        # Calculate Max Safe Loan based on FOIR (Max monthly EMI allowed)
        max_foir = loan_meta["max_foir"]
        max_allowed_emi = income * max_foir
        typical_rate = loan_meta["avg_rate"]
        max_years = loan_meta["max_tenure_years"]

        # Inverse EMI calculation to estimate max safe principal
        m_rate = typical_rate / (12 * 100)
        t_months = max_years * 12
        max_safe_principal = (max_allowed_emi * (((1 + m_rate)**t_months) - 1)) / (m_rate * ((1 + m_rate)**t_months))

        rec_emi, rec_int, _ = calculate_emi(max_safe_principal, typical_rate, max_years)

        # Recommendation Cards
        rc1, rc2 = st.columns(2)
        with rc1:
            st.markdown(
                f"""
                <div class="fb-card">
                    <div class="fb-card-header">📋 {get_text('rec_loan_type', lang)}</div>
                    <div style="font-size:1.3rem; font-weight:700; color:#1E3A8A;">{selected_purpose_name}</div>
                    <p style="margin-top:8px; color:#64748B;">
                        • {get_text('rec_interest', lang)}: <b>{typical_rate}% - {typical_rate + 2.5}% p.a.</b><br>
                        • Recommended Max Tenure: <b>{max_years} {get_text('years_unit', lang)}</b>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with rc2:
            st.markdown(
                f"""
                <div class="fb-card">
                    <div class="fb-card-header">💰 {get_text('max_safe_loan', lang)}</div>
                    <div style="font-size:1.8rem; font-weight:800; color:#10B981;">₹{max_safe_principal:,.0f}</div>
                    <p style="margin-top:8px; color:#64748B;">
                        Approx. Safe Monthly EMI: <b>₹{rec_emi:,.0f}/mo</b><br>
                        (Strictly keeps your total EMI under {int(max_foir*100)}% of monthly salary)
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Loan Safety & Direct Bank Disbursal Section (Always visible)
    st.markdown("---")
    st.markdown(
        f"""
        <div class="fb-safety-box">
            <h4>{get_text('loan_safety_header', lang)}</h4>
            <p><b>❓ {get_text('bank_transfer_safe', lang)}</b></p>
            <p style="background:#FFFFFF; padding:12px; border-radius:10px; border:1px solid #A7F3D0;">
                {get_text('bank_transfer_answer', lang)}
            </p>
            <div style="margin-top:14px;">
                <div class="fb-safety-item">{get_text('safety_tip1', lang)}</div>
                <div class="fb-safety-item">{get_text('safety_tip2', lang)}</div>
                <div class="fb-safety-item">{get_text('safety_tip3', lang)}</div>
                <div class="fb-safety-item">{get_text('safety_tip4', lang)}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
