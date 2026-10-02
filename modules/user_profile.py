"""
User Profile Management and Money Health Score Logic
"""

import streamlit as st
from translations import get_text

def init_user_profile():
    """Initialize default user profile in st.session_state if not present."""
    if "user_profile" not in st.session_state:
        st.session_state.user_profile = {
            "income": 50000.0,
            "expenses": 30000.0,
            "age": 28,
            "city": "Mumbai",
            "goal": "Build Emergency Fund",
            "is_setup": True
        }

def calculate_health_score(income: float, expenses: float) -> dict:
    """
    Calculate Money Health Score (0-100) based on financial metrics.
    Returns score, status text, color class, and actionable recommendations.
    """
    if income <= 0:
        return {
            "score": 0,
            "status_key": "status_critical",
            "color_class": "score-red",
            "savings_ratio": 0.0,
            "surplus": 0.0,
            "tips": ["Income must be greater than zero to calculate financial health."]
        }
    
    surplus = income - expenses
    savings_ratio = (surplus / income) * 100
    expense_ratio = (expenses / income) * 100

    score = 0

    # 1. Savings Ratio Score (Max 40 points)
    if savings_ratio >= 35:
        score += 40
    elif savings_ratio >= 25:
        score += 32
    elif savings_ratio >= 15:
        score += 22
    elif savings_ratio >= 5:
        score += 12
    elif savings_ratio > 0:
        score += 5

    # 2. Expense Ratio Score (Max 35 points)
    if expense_ratio <= 45:
        score += 35
    elif expense_ratio <= 60:
        score += 28
    elif expense_ratio <= 75:
        score += 18
    elif expense_ratio <= 90:
        score += 8

    # 3. Monthly Surplus Absolute Value (Max 15 points)
    if surplus >= 25000:
        score += 15
    elif surplus >= 10000:
        score += 12
    elif surplus >= 5000:
        score += 8
    elif surplus > 0:
        score += 4

    # 4. Financial Buffer Stability (Max 10 points)
    if expense_ratio < 70 and surplus > 0:
        score += 10

    score = min(100, max(0, score))

    # Determine status & color
    if score >= 80:
        status_key = "status_excellent"
        color_class = "score-green"
        color_code = "#10B981"
    elif score >= 60:
        status_key = "status_good"
        color_class = "score-green"
        color_code = "#059669"
    elif score >= 40:
        status_key = "status_average"
        color_class = "score-yellow"
        color_code = "#F59E0B"
    else:
        status_key = "status_critical"
        color_class = "score-red"
        color_code = "#EF4444"

    # Dynamic Tips based on score breakdown
    tips = []
    if expense_ratio > 70:
        tips.append("Your expenses take up over 70% of your income. Look into reducing non-essential expenses.")
    if savings_ratio < 20:
        tips.append("Aim to save at least 20% of your monthly salary following the 50/30/20 rule.")
    if surplus <= 0:
        tips.append("Danger zone! Expenses equal or exceed income. Avoid taking any new loan EMIs immediately.")
    if savings_ratio >= 30:
        tips.append("Fantastic savings rate! Consider putting your surplus into mutual funds or fixed deposits for wealth growth.")

    if not tips:
        tips.append("Maintain your good financial discipline and keep investing your monthly surplus regularly!")

    return {
        "score": score,
        "status_key": status_key,
        "color_class": color_class,
        "color_code": color_code,
        "savings_ratio": round(savings_ratio, 1),
        "expense_ratio": round(expense_ratio, 1),
        "surplus": round(surplus, 2),
        "tips": tips
    }

def render_profile_sidebar(lang: str):
    """Render profile form and summary in the Streamlit sidebar."""
    init_user_profile()
    profile = st.session_state.user_profile

    st.sidebar.markdown(f"### {get_text('profile_title', lang)}")
    st.sidebar.caption(get_text("profile_subtitle", lang))

    with st.sidebar.expander(get_text("profile_title", lang), expanded=False):
        with st.form("sidebar_profile_form"):
            income = st.number_input(
                get_text("monthly_income", lang),
                min_value=0.0,
                value=float(profile.get("income", 50000.0)),
                step=1000.0
            )
            expenses = st.number_input(
                get_text("monthly_expenses", lang),
                min_value=0.0,
                value=float(profile.get("expenses", 30000.0)),
                step=1000.0
            )
            age = st.number_input(
                get_text("age", lang),
                min_value=18,
                max_value=100,
                value=int(profile.get("age", 28))
            )
            city = st.text_input(
                get_text("city", lang),
                value=str(profile.get("city", "Mumbai"))
            )

            goals = [
                get_text("goal_emergency", lang),
                get_text("goal_bike", lang),
                get_text("goal_gadget", lang),
                get_text("goal_home", lang),
                get_text("goal_education", lang),
                get_text("goal_retirement", lang),
                get_text("goal_debt_free", lang)
            ]
            goal = st.selectbox(
                get_text("financial_goal", lang),
                options=goals,
                index=0
            )

            submitted = st.form_submit_button(get_text("save_profile", lang), use_container_width=True, type="primary")

            if submitted:
                st.session_state.user_profile = {
                    "income": income,
                    "expenses": expenses,
                    "age": age,
                    "city": city,
                    "goal": goal,
                    "is_setup": True
                }
                st.sidebar.success(get_text("profile_saved", lang))
                st.rerun()

    # Quick Summary Display
    curr_income = st.session_state.user_profile["income"]
    curr_expenses = st.session_state.user_profile["expenses"]
    surplus = curr_income - curr_expenses

    st.sidebar.markdown(f"#### 📊 {get_text('profile_summary', lang)}")
    col_a, col_b = st.sidebar.columns(2)
    col_a.metric(get_text("income_lbl", lang), f"₹{curr_income:,.0f}")
    col_b.metric(get_text("expense_lbl", lang), f"₹{curr_expenses:,.0f}")
    
    surplus_color = "normal" if surplus >= 0 else "inverse"
    st.sidebar.metric(get_text("savings_lbl", lang), f"₹{surplus:,.0f}", delta=f"{((surplus/curr_income)*100 if curr_income>0 else 0):.1f}%", delta_color=surplus_color)

    # Health score miniature in sidebar
    health_data = calculate_health_score(curr_income, curr_expenses)
    st.sidebar.markdown(
        f"""
        <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:12px; padding:12px; text-align:center; margin-top:12px;">
            <div style="font-size:0.8rem; color:#166534; font-weight:600;">{get_text('health_score_title', lang)}</div>
            <div style="font-size:2rem; font-weight:800; color:{health_data['color_code']};">{health_data['score']}/100</div>
            <div style="font-size:0.85rem; font-weight:600; color:#1E293B;">{get_text(health_data['status_key'], lang)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
