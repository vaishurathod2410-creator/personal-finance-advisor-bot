# 💰 FineBuddy - Personal Finance Advisor Bot

**FineBuddy** is a modern, full-featured Personal Finance Advisor web application built with **Streamlit**, designed to empower normal everyday individuals with smart budgeting, savings goal tracking, EMI calculations, safe loan recommendations, multi-lingual AI financial advice (English, Hindi, Marathi), and downloadable PDF report generation.

---

## ✨ Features Overview

1. **💬 Multi-lingual AI Financial Advisor (Chat)**
   - Conversational AI advisor with friendly, empathetic, plain-language guidance.
   - Session chat memory to remember previous messages in the session.
   - Quick question chips for instant guidance on salary allocation, smartphone loans, emergency funds, and safe EMI limits.

2. **🌐 Full Multi-Language Support (English, Hindi, Marathi)**
   - English (Default), Hindi (हिंदी), Marathi (मराठी).
   - Dynamic sidebar language switcher that instantly translates all UI text, buttons, metric cards, bot replies, and downloadable PDF reports.

3. **👤 User Profile & Sidebar Control**
   - Collects and manages Monthly Income, Monthly Expenses, Age, City, and Primary Financial Goal.
   - Instantly updates disposable income (surplus) and Money Health Score metrics.

4. **📊 Personalized Budget Maker (50/30/20 Rule)**
   - Calculates recommended allocation for Needs (50%), Wants (30%), and Savings (20%).
   - Interactive category spending breakdown (Rent, Food, Bills, Transport, Entertainment, Misc).
   - Interactive Plotly Donut Chart (Expense Distribution) & Bar Chart (Recommended vs Actual comparison).

5. **🎯 Savings Goal Tracker & 🔮 "What-If" Analysis**
   - Goal progress bar, monthly required savings, and target date calculator.
   - Interactive "What-If" slider: See how saving extra money each month accelerates goal achievement and projects wealth growth @ 8% p.a. returns over time with line chart trajectories.

6. **🧮 EMI Calculator & 🏦 Safe Loan Recommender**
   - **EMI Calculator:** Principal, Interest Rate, Tenure, Monthly EMI, Total Interest, Principal vs Interest Pie Chart, and EMI Affordability Index (<35% Safe, 35-50% Moderate, >50% Risky).
   - **Loan Recommender:** Tailored suggestions for Bike/Scooter, Phone/Gadget, Home, Education, and Personal Loans based on income and FOIR limits.
   - **🛡️ Direct Bank Transfer & Safety Guidelines:** Detailed advice explaining how real banks/NBFCs transfer funds directly to salary accounts via NEFT/RTGS/IMPS, avoiding advance fee scams and illegal apps.

7. **💯 Money Health Score (0 - 100)**
   - Calculated dynamically based on savings ratio, expense burden, and surplus safety buffer.

8. **📄 Downloadable PDF Blueprint Report**
   - One-click ReportLab PDF generation containing profile snapshot, Money Health Score, budget table, safe loan limits, and personalized action tips.

---

## 📁 Project Architecture

```
FineBuddy/
├── app.py                      # Main Streamlit Application Entrypoint
├── config.py                   # App Configuration, Theme Colors & Loan Metadata
├── translations.py             # Full English, Hindi, and Marathi Dictionaries
├── assets/
│   └── style.css               # Modern Soft Blue, White & Green Accent Theme CSS
├── modules/
│   ├── user_profile.py         # Profile Management & Money Health Score Engine
│   ├── budget_maker.py         # 50/30/20 Budgeting & Plotly Visualizations
│   ├── savings_tracker.py      # Savings Tracker & What-If Analyzer
│   ├── emi_loan.py             # EMI Calculator, Loan Recommender & Bank Safety Tips
│   ├── advisor_bot.py          # AI Financial Advisor Chat Engine & Memory
│   └── pdf_generator.py        # ReportLab PDF Report Generator
└── README.md                   # Documentation & How-to Run Guide
```

---

## 🚀 Quick Start Guide

### 1. Install Dependencies
```bash
pip install streamlit reportlab plotly pandas numpy pillow
```

### 2. Launch Application
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`.
