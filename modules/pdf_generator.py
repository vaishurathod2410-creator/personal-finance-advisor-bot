"""
PDF Report Generator using ReportLab for FineBuddy
"""

import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from translations import get_text
from modules.user_profile import calculate_health_score

def generate_pdf_report(lang: str) -> bytes:
    """Generate a clean, styled PDF financial blueprint report as bytes."""
    profile = st_profile = getattr(generate_pdf_report, "_profile", None)
    
    # Access session state profile
    import streamlit as st
    profile = st.session_state.user_profile
    income = profile.get("income", 50000.0)
    expenses = profile.get("expenses", 30000.0)
    surplus = max(0.0, income - expenses)
    age = profile.get("age", 28)
    city = profile.get("city", "Mumbai")
    goal = profile.get("goal", "Build Emergency Fund")

    health = calculate_health_score(income, expenses)

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        textColor=colors.HexColor('#1E3A8A'),
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        textColor=colors.HexColor('#64748B'),
        spaceAfter=15
    )

    h2_style = ParagraphStyle(
        'Heading2Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=12,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        textColor=colors.HexColor('#1E293B'),
        leading=14
    )

    bold_body = ParagraphStyle(
        'BoldBody',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    story = []

    # Title Banner
    story.append(Paragraph("FineBuddy - Personal Finance Report", title_style))
    story.append(Paragraph("Your Comprehensive Financial Health Blueprint & Advisory Summary", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#2563EB'), spaceAfter=15))

    # Profile & Health Summary Table
    story.append(Paragraph("1. User Profile & Money Health Summary", h2_style))
    
    profile_data = [
        [Paragraph("Monthly Income", bold_body), Paragraph(f"Rs. {income:,.0f}", body_style),
         Paragraph("Monthly Expenses", bold_body), Paragraph(f"Rs. {expenses:,.0f}", body_style)],
        [Paragraph("Monthly Surplus", bold_body), Paragraph(f"Rs. {surplus:,.0f}", body_style),
         Paragraph("Age / Location", bold_body), Paragraph(f"{age} yrs / {city}", body_style)],
        [Paragraph("Primary Goal", bold_body), Paragraph(f"{goal}", body_style),
         Paragraph("Money Health Score", bold_body), Paragraph(f"{health['score']}/100 ({get_text(health['status_key'], 'English')})", bold_body)]
    ]

    t_profile = Table(profile_data, colWidths=[120, 150, 120, 150])
    t_profile.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_profile)
    story.append(Spacer(1, 12))

    # 50/30/20 Budget Breakdown Table
    story.append(Paragraph("2. 50/30/20 Budget Allocation Plan", h2_style))
    
    rec_needs = income * 0.50
    rec_wants = income * 0.30
    rec_savings = income * 0.20

    budget_table_data = [
        [Paragraph("Category", bold_body), Paragraph("Target %", bold_body), Paragraph("Recommended Amount", bold_body), Paragraph("Status", bold_body)],
        [Paragraph("Needs (Rent, Bills, Food)", body_style), Paragraph("50%", body_style), Paragraph(f"Rs. {rec_needs:,.0f}", body_style), Paragraph("Essential Living", body_style)],
        [Paragraph("Wants (Lifestyle, Dining)", body_style), Paragraph("30%", body_style), Paragraph(f"Rs. {rec_wants:,.0f}", body_style), Paragraph("Discretionary", body_style)],
        [Paragraph("Savings & Investments", body_style), Paragraph("20%", body_style), Paragraph(f"Rs. {rec_savings:,.0f}", body_style), Paragraph("Wealth Creation", body_style)]
    ]

    t_budget = Table(budget_table_data, colWidths=[160, 80, 160, 140])
    t_budget.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EFF6FF')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_budget)
    story.append(Spacer(1, 12))

    # Loan Safety & Recommendations
    story.append(Paragraph("3. Loan Safety & Safe Affordability Limits", h2_style))
    max_safe_emi = income * 0.35
    
    loan_text = (
        f"<b>Maximum Safe Monthly EMI:</b> Rs. {max_safe_emi:,.0f} (35% FOIR cap)<br/>"
        f"<b>Bank Disbursal Safety Rule:</b> Legitimate loans from RBI-registered banks/NBFCs are always disbursed "
        f"directly into your verified bank account via NEFT/IMPS. Real lenders NEVER charge advance processing fees in cash!"
    )
    story.append(Paragraph(loan_text, body_style))
    story.append(Spacer(1, 12))

    # Actionable Tips Section
    story.append(Paragraph("4. FineBuddy Advisor Key Recommendations", h2_style))
    for tip in health["tips"]:
        story.append(Paragraph(f"• {tip}", body_style))

    story.append(Spacer(1, 20))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#E2E8F0'), spaceAfter=10))
    story.append(Paragraph("Generated by FineBuddy Personal Finance Advisor Bot • Keep saving, keep growing!", subtitle_style))

    doc.build(story)
    return buffer.getvalue()

def render_report_view(lang: str):
    """Render PDF Report download page."""
    import streamlit as st
    st.markdown(f"## {get_text('report_title', lang)}")
    st.caption(get_text("report_desc", lang))

    st.markdown("<div class='fb-card' style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("### 📋 Your Financial Summary Package")
    st.write("Includes: User Profile, Money Health Score, 50/30/20 Budget Plan, Safe Loan Limits, and Action Tips.")

    pdf_bytes = generate_pdf_report(lang)

    st.download_button(
        label=get_text("generate_pdf_btn", lang),
        data=pdf_bytes,
        file_name="FineBuddy_Financial_Report.pdf",
        mime="application/pdf",
        use_container_width=True,
        type="primary"
    )
    st.markdown("</div>", unsafe_allow_html=True)
