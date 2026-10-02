"""
FineBuddy - Personal Finance Advisor Bot
Main Streamlit Application Entry Point
"""

import os
import streamlit as st

# Page configuration - MUST BE FIRST STREAMLIT CALL
st.set_page_config(
    page_title="FineBuddy - Personal Finance Advisor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Custom CSS styling
css_path = os.path.join(os.path.dirname(__file__), "assets", "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from translations import get_text, LANGUAGES
from modules.user_profile import init_user_profile, render_profile_sidebar, calculate_health_score
from modules.budget_maker import render_budget_maker
from modules.savings_tracker import render_savings_tracker
from modules.emi_loan import render_emi_loan
from modules.advisor_bot import render_chat_interface
from modules.pdf_generator import render_report_view

def main():
    # Initialize session state language
    if "language" not in st.session_state:
        st.session_state.language = "English"

    # Sidebar Header & Language Switcher
    st.sidebar.markdown(
        """
        <div style="text-align: center; padding-bottom: 15px; border-bottom: 1px solid #E2E8F0; margin-bottom: 15px;">
            <h2 style="color: #1E3A8A; margin: 0; font-weight: 800;">💰 FineBuddy</h2>
            <p style="color: #64748B; font-size: 0.85rem; margin-top: 2px; margin-bottom: 0;">Personal Finance Advisor</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Language Dropdown Selector
    selected_lang_display = st.sidebar.selectbox(
        get_text("lang_select", st.session_state.language),
        options=list(LANGUAGES.values()),
        index=list(LANGUAGES.keys()).index(st.session_state.language)
    )

    # Update session state if language changed
    for eng_name, disp_name in LANGUAGES.items():
        if disp_name == selected_lang_display:
            if st.session_state.language != eng_name:
                st.session_state.language = eng_name
                st.rerun()

    current_lang = st.session_state.language

    # Render Sidebar User Profile & Health Score
    render_profile_sidebar(current_lang)

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"#### 🧭 Navigation")

    # Navigation Options
    nav_options = [
        get_text("nav_chat", current_lang),
        get_text("nav_budget", current_lang),
        get_text("nav_savings", current_lang),
        get_text("nav_emi_loan", current_lang),
        get_text("nav_report", current_lang)
    ]

    selected_nav = st.sidebar.radio(
        "Go to",
        options=nav_options,
        label_visibility="collapsed"
    )

    # Main Content Hero Header Banner
    st.markdown(
        f"""
        <div class="fb-hero">
            <h1>{get_text('app_title', current_lang)}</h1>
            <p>{get_text('app_tagline', current_lang)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Router to Selected Feature View
    if selected_nav == get_text("nav_chat", current_lang):
        render_chat_interface(current_lang)
    elif selected_nav == get_text("nav_budget", current_lang):
        render_budget_maker(current_lang)
    elif selected_nav == get_text("nav_savings", current_lang):
        render_savings_tracker(current_lang)
    elif selected_nav == get_text("nav_emi_loan", current_lang):
        render_emi_loan(current_lang)
    elif selected_nav == get_text("nav_report", current_lang):
        render_report_view(current_lang)

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; color: #94A3B8; font-size: 0.85rem; padding: 10px 0;">
            FineBuddy © 2026 • Built for everyday financial empowerment • English | हिंदी | मराठी
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
