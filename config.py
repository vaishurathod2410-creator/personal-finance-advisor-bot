"""
Configuration and Constants for FineBuddy Personal Finance Advisor Bot
"""

APP_NAME = "FineBuddy"
APP_SUBTITLE = "Personal Finance Advisor Bot"
DEFAULT_LANG = "English"

LANGUAGES = {
    "English": "English",
    "Hindi": "हिंदी",
    "Marathi": "मराठी"
}

# Color Theme definitions
COLORS = {
    "primary": "#2563EB",       # Soft/Royal Blue
    "primary_dark": "#1E3A8A",  # Dark Blue
    "secondary": "#10B981",     # Soft Green Accent
    "secondary_dark": "#059669",
    "bg_light": "#F8FAFC",      # Clean soft background
    "card_bg": "#FFFFFF",       # Card background
    "text_dark": "#1E293B",     # Main body text
    "text_muted": "#64748B",    # Muted text
    "warning": "#F59E0B",      # Warm Amber
    "danger": "#EF4444",       # Coral Red
    "accent_blue": "#EFF6FF"
}

# Standard 50/30/20 Budget Guidelines
BUDGET_RULES = {
    "needs_pct": 50,
    "wants_pct": 30,
    "savings_pct": 20
}

# Default Loan Types and typical Indian Market interest rates
LOAN_TYPES = {
    "bike": {
        "name_en": "Two-Wheeler / Bike Loan",
        "name_hi": "टू-व्हीलर / बाइक लोन",
        "name_mr": "टू-व्हीलर / बाईक कर्ज",
        "avg_rate": 10.5,
        "max_tenure_years": 4,
        "max_foir": 0.40  # Max total EMI should not exceed 40% of income
    },
    "phone": {
        "name_en": "Gadget / Phone No-Cost EMI",
        "name_hi": "गैजेट / फोन नो-कॉस्ट ईएमआई",
        "name_mr": "गॅझेट / फोन नो-कॉस्ट ईएमआय",
        "avg_rate": 13.0,
        "max_tenure_years": 1,
        "max_foir": 0.25
    },
    "house": {
        "name_en": "Home Loan / Housing Finance",
        "name_hi": "होम लोन / आवास वित्त",
        "name_mr": "होम लोन / गृहकर्ज",
        "avg_rate": 8.5,
        "max_tenure_years": 30,
        "max_foir": 0.50
    },
    "education": {
        "name_en": "Education / Student Loan",
        "name_hi": "शिक्षा ऋण / स्टूडेंट लोन",
        "name_mr": "शिक्षण कर्ज / विद्यार्थी कर्ज",
        "avg_rate": 9.0,
        "max_tenure_years": 10,
        "max_foir": 0.45
    },
    "personal": {
        "name_en": "Personal Loan",
        "name_hi": "व्यक्तिगत ऋण / पर्सनल लोन",
        "name_mr": "वैयक्तिक कर्ज / पर्सनल लोन",
        "avg_rate": 12.5,
        "max_tenure_years": 5,
        "max_foir": 0.35
    }
}
