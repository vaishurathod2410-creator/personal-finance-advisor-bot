"""
Full multi-language dictionary and translation helper for FineBuddy (English, Hindi, Marathi)
"""

LANGUAGES = {
    "English": "English",
    "Hindi": "हिंदी",
    "Marathi": "मराठी"
}

TRANSLATIONS = {
    "English": {
        # App Header & Navigation
        "app_title": "FineBuddy",
        "app_tagline": "Your Smart & Friendly Personal Finance Advisor",
        "lang_select": "🌐 Choose Language",
        "nav_chat": "💬 AI Financial Advisor",
        "nav_budget": "📊 Budget & Health Score",
        "nav_savings": "🎯 Savings & What-If",
        "nav_emi_loan": "🧮 EMI & Safe Loans",
        "nav_report": "📄 Download Report",

        # Profile Sidebar
        "profile_title": "👤 User Financial Profile",
        "profile_subtitle": "Keep your profile updated for accurate advice",
        "monthly_income": "Monthly Income (₹)",
        "monthly_expenses": "Monthly Expenses (₹)",
        "age": "Age (Years)",
        "city": "City / Location",
        "financial_goal": "Primary Financial Goal",
        "save_profile": "💾 Save Profile",
        "profile_saved": "✅ Profile saved successfully!",
        "profile_summary": "Profile Summary",
        "income_lbl": "Income",
        "expense_lbl": "Expenses",
        "savings_lbl": "Monthly Surplus",

        # Health Score
        "health_score_title": "Money Health Score",
        "health_score_desc": "Calculated based on your savings ratio, income-expense balance, and financial safety margin.",
        "score_label": "Financial Health Index",
        "status_excellent": "🌟 Excellent Financial Fitness!",
        "status_good": "👍 Good & Stable",
        "status_average": "⚠️ Needs Improvement",
        "status_critical": "🚨 Action Required!",
        "tip_title": "💡 Tip to Boost Score",

        # Goals Options
        "goal_emergency": "Build Emergency Fund",
        "goal_bike": "Buy a Bike / Scooter",
        "goal_gadget": "Buy Phone / Laptop",
        "goal_home": "Save for House Down Payment",
        "goal_education": "Higher Education",
        "goal_retirement": "Long-Term Retirement",
        "goal_debt_free": "Become Debt-Free",

        # Budget Maker
        "budget_title": "📊 Personalized Budget Maker",
        "budget_desc": "Based on the proven 50/30/20 financial rule customized for your income.",
        "needs_label": "Needs (Rent, Groceries, Bills, Medicine - 50%)",
        "wants_label": "Wants (Dining out, Shopping, Movies - 30%)",
        "savings_invest_label": "Savings & Investments (20%)",
        "actual_spending": "Your Current Spending",
        "recommended_spending": "Recommended 50/30/20 Plan",
        "category_breakdown": "Custom Expense Breakdown",
        "rent_housing": "Rent / Housing",
        "food_groceries": "Food & Groceries",
        "utilities_bills": "Utilities & Bills",
        "transport": "Transport / Fuel",
        "entertainment": "Entertainment & Lifestyle",
        "misc": "Other Expenses",
        "budget_analysis": "Smart Budget Advice",

        # Savings & What-If
        "savings_title": "🎯 Savings Goal Tracker",
        "savings_desc": "Set your targets and see how fast you can achieve your dreams.",
        "target_amount": "Target Goal Amount (₹)",
        "current_saved": "Already Saved Amount (₹)",
        "target_months": "Desired Timeframe (Months)",
        "monthly_req": "Required Monthly Saving",
        "available_surplus": "Your Current Surplus",
        "goal_achievable": "🎉 Great job! Your monthly surplus easily covers this target.",
        "goal_tight": "⚠️ Target is achievable, but requires saving a bit more each month.",
        "goal_overbudget": "🚨 Your required monthly saving exceeds your current surplus. Consider extending the duration or reducing expenses.",
        "what_if_title": "🔮 'What-If' Scenario Analyzer",
        "what_if_desc": "See how saving just a little extra each month dramatically accelerates your goals!",
        "extra_save_label": "What if you save an EXTRA amount every month? (₹)",
        "what_if_result_months": "Months saved to reach goal",
        "what_if_interest_growth": "Est. wealth growth if invested @ 8% p.a.",

        # EMI & Safe Loans
        "emi_title": "🧮 EMI Calculator & Loan Safety Check",
        "loan_amount_label": "Loan Amount (₹)",
        "interest_rate_label": "Annual Interest Rate (%)",
        "tenure_label": "Loan Tenure (Years)",
        "calculate_emi_btn": "Calculate EMI",
        "monthly_emi_result": "Monthly EMI",
        "total_interest_result": "Total Interest",
        "total_payment_result": "Total Payment",
        "emi_affordability": "EMI Affordability Index",
        "safe_emi": "✅ Safe EMI: Less than 35% of your income. Highly affordable!",
        "moderate_emi": "⚠️ Moderate EMI: 35-50% of income. Watch out for other expenses.",
        "risky_emi": "🚨 High Risk EMI: Exceeds 50% of monthly income. Highly discouraged!",
        
        "loan_recommend_title": "🏦 Smart Loan Recommender",
        "loan_purpose_label": "Select Loan Need / Purpose",
        "recommend_btn": "Get Loan Recommendation",
        "max_safe_loan": "Max Safe Loan Limit for Your Income",
        "rec_loan_type": "Recommended Loan Category",
        "rec_interest": "Typical Interest Rate Range",
        
        # Loan Safety & Bank Transfer
        "loan_safety_header": "🛡️ Bank Disbursal & Fraud Prevention Guidelines",
        "bank_transfer_safe": "Is the loan amount safely transferred to your bank account?",
        "bank_transfer_answer": "Yes! Legitimate RBI-regulated banks and NBFCs directly transfer approved loan funds straight into your verified bank account via NEFT/RTGS/IMPS.",
        "safety_tip1": "<b>1. Verify RBI License:</b> Always take loans only from RBI-registered banks or NBFCs. Avoid unauthorized mobile loan apps.",
        "safety_tip2": "<b>2. No Advance Fee Scam:</b> Real banks NEVER ask for cash or upfront fees to release your loan.",
        "safety_tip3": "<b>3. Direct Bank Disbursal:</b> Ensure the loan agreement clearly specifies disbursal directly to your salary account.",
        "safety_tip4": "<b>4. Protect OTP & PIN:</b> Never share bank password, OTP, or PIN with anyone claiming to be a loan agent.",

        # Chat Interface
        "chat_title": "💬 Chat with FineBuddy",
        "chat_welcome": "Hello! 👋 I'm FineBuddy, your friendly personal finance companion. Ask me anything about savings, budgeting, loans, emergency funds, or managing daily expenses!",
        "chat_placeholder": "Type your message or question here...",
        "quick_questions": "💡 Quick Questions:",
        "q1": "How should I allocate my salary every month?",
        "q2": "Is it safe to take a personal loan for a smartphone?",
        "q3": "How can I build an emergency fund quickly?",
        "q4": "How much loan EMI can I safely afford?",

        # PDF Report
        "report_title": "📄 Download Your Personalized Financial Blueprint",
        "report_desc": "Get a complete PDF summary containing your Money Health Score, Budget Breakdown, Savings Roadmap, Loan Analysis, and Advisor Tips.",
        "generate_pdf_btn": "📥 Generate & Download PDF Report",
        "pdf_success": "✅ Your PDF Report has been generated!",

        # General Buttons & Words
        "currency_symbol": "₹",
        "months_unit": "Months",
        "years_unit": "Years",
        "per_month": "/month"
    },

    "Hindi": {
        # App Header & Navigation
        "app_title": "फाइनबडी (FineBuddy)",
        "app_tagline": "आपका समझदार और मित्रवत व्यक्तिगत वित्त सलाहकार",
        "lang_select": "🌐 भाषा चुनें",
        "nav_chat": "💬 एआई वित्तीय सलाहकार",
        "nav_budget": "📊 बजट और हेल्थ स्कोर",
        "nav_savings": "🎯 बचत और वाट-इफ",
        "nav_emi_loan": "🧮 ईएमआई और सुरक्षित ऋण",
        "nav_report": "📄 रिपोर्ट डाउनलोड करें",

        # Profile Sidebar
        "profile_title": "👤 उपयोगकर्ता वित्तीय प्रोफ़ाइल",
        "profile_subtitle": "सटीक सलाह के लिए अपनी प्रोफ़ाइल अपडेट रखें",
        "monthly_income": "मासिक आय (₹)",
        "monthly_expenses": "मासिक खर्च (₹)",
        "age": "आयु (वर्ष)",
        "city": "शहर / स्थान",
        "financial_goal": "मुख्य वित्तीय लक्ष्य",
        "save_profile": "💾 प्रोफ़ाइल सहेजें",
        "profile_saved": "✅ प्रोफ़ाइल सफलतापूर्वक सहेजी गई!",
        "profile_summary": "प्रोफ़ाइल सारांश",
        "income_lbl": "आय",
        "expense_lbl": "खर्च",
        "savings_lbl": "मासिक बचत (सरप्लस)",

        # Health Score
        "health_score_title": "मनी हेल्थ स्कोर (Money Health Score)",
        "health_score_desc": "आपकी बचत दर, आय-खर्च संतुलन और वित्तीय सुरक्षा मार्जिन के आधार पर गणना की गई।",
        "score_label": "वित्तीय स्वास्थ्य सूचकांक",
        "status_excellent": "🌟 उत्कृष्ट वित्तीय स्थिति!",
        "status_good": "👍 अच्छी और स्थिर स्थिति",
        "status_average": "⚠️ ध्यान देने की आवश्यकता",
        "status_critical": "🚨 तुरंत सुधार की आवश्यकता!",
        "tip_title": "💡 स्कोर बढ़ाने का सुझाव",

        # Goals Options
        "goal_emergency": "आपातकालीन फंड (Emergency Fund) बनाएं",
        "goal_bike": "बाइक / स्कूटर खरीदें",
        "goal_gadget": "फोन / लैपटॉप खरीदें",
        "goal_home": "घर की डाउन पेमेंट के लिए बचत करें",
        "goal_education": "उच्च शिक्षा (Higher Education)",
        "goal_retirement": "दीर्घकालिक सेवानिवृत्ति (Retirement)",
        "goal_debt_free": "कर्ज मुक्त (Debt-Free) बनें",

        # Budget Maker
        "budget_title": "📊 व्यक्तिगत बजट निर्माता",
        "budget_desc": "आपकी आय के अनुसार अनुकूलित 50/30/20 नियम पर आधारित।",
        "needs_label": "आवश्यकताएं (किराया, राशन, बिल, दवा - 50%)",
        "wants_label": "इच्छाएं (बाहर खाना, खरीदारी, फिल्में - 30%)",
        "savings_invest_label": "बचत और निवेश (20%)",
        "actual_spending": "आपका वर्तमान खर्च",
        "recommended_spending": "अनुशंसित 50/30/20 योजना",
        "category_breakdown": "विस्तृत खर्च विभाजन",
        "rent_housing": "किराया / घर खर्च",
        "food_groceries": "भोजन और राशन",
        "utilities_bills": "बिजली, पानी व अन्य बिल",
        "transport": "यातायात / पेट्रोल",
        "entertainment": "मनोरंजन और लाइफस्टाइल",
        "misc": "अन्य खर्च",
        "budget_analysis": "स्मार्ट बजट सलाह",

        # Savings & What-If
        "savings_title": "🎯 बचत लक्ष्य ट्रैकर",
        "savings_desc": "अपने लक्ष्य निर्धारित करें और देखें कि आप अपने सपनों को कितनी जल्दी पूरा कर सकते हैं।",
        "target_amount": "लक्ष्य राशि (₹)",
        "current_saved": "अब तक बचाई गई राशि (₹)",
        "target_months": "समय सीमा (महीने)",
        "monthly_req": "आवश्यक मासिक बचत",
        "available_surplus": "आपकी वर्तमान मासिक बचत",
        "goal_achievable": "🎉 बहुत बढ़िया! आपकी वर्तमान बचत आसानी से इस लक्ष्य को पूरा कर सकती है।",
        "goal_tight": "⚠️ लक्ष्य प्राप्त किया जा सकता है, लेकिन हर महीने थोड़ा अधिक बचाने की आवश्यकता है।",
        "goal_overbudget": "🚨 आवश्यक मासिक बचत आपकी वर्तमान आय बचत से अधिक है। समय सीमा बढ़ाने या खर्च घटाने पर विचार करें।",
        "what_if_title": "🔮 'व्हाट-इफ' (What-If) विश्लेषण",
        "what_if_desc": "देखें कि हर महीने थोड़ी अतिरिक्त बचत आपके लक्ष्यों को कितनी तेजी से पूरा करती है!",
        "extra_save_label": "यदि आप हर महीने अतिरिक्त राशि बचाते हैं: (₹)",
        "what_if_result_months": "लक्ष्य तक पहुँचने में बचे महीने",
        "what_if_interest_growth": "8% वार्षिक ब्याज दर पर अनुमानित संपत्ति वृद्धि",

        # EMI & Safe Loans
        "emi_title": "🧮 ईएमआई कैलकुलेटर और ऋण सुरक्षा जांच",
        "loan_amount_label": "ऋण राशि (₹)",
        "interest_rate_label": "वार्षिक ब्याज दर (%)",
        "tenure_label": "ऋण अवधि (वर्ष)",
        "calculate_emi_btn": "ईएमआई की गणना करें",
        "monthly_emi_result": "मासिक ईएमआई",
        "total_interest_result": "कुल देय ब्याज",
        "total_payment_result": "कुल भुगतान",
        "emi_affordability": "ईएमआई वहन क्षमता (Affordability)",
        "safe_emi": "✅ सुरक्षित ईएमआई: आपकी आय के 35% से कम। बहुत आसानी से देय!",
        "moderate_emi": "⚠️ मध्यम ईएमआई: आय का 35-50%। अन्य खर्चों पर ध्यान दें।",
        "risky_emi": "🚨 उच्च जोखिम ईएमआई: मासिक आय के 50% से अधिक। सलाह नहीं दी जाती!",
        
        "loan_recommend_title": "🏦 स्मार्ट ऋण अनुशंसा प्रणाली",
        "loan_purpose_label": "ऋण का उद्देश्य / आवश्यकता चुनें",
        "recommend_btn": "ऋण सुझाव प्राप्त करें",
        "max_safe_loan": "आपकी आय के अनुसार अधिकतम सुरक्षित ऋण सीमा",
        "rec_loan_type": "अनुशंसित ऋण प्रकार",
        "rec_interest": "सामान्य ब्याज दर सीमा",
        
        # Loan Safety & Bank Transfer
        "loan_safety_header": "🛡️ बैंक ट्रांसफर सुरक्षा और धोखाधड़ी से बचाव",
        "bank_transfer_safe": "क्या ऋण राशि सुरक्षित रूप से आपके बैंक खाते में स्थानांतरित की जाएगी?",
        "bank_transfer_answer": "हाँ! भारतीय रिजर्व बैंक (RBI) द्वारा पंजीकृत बैंक और NBFC स्वीकृत ऋण राशि सीधे आपके सत्यापित बैंक खाते में NEFT/RTGS/IMPS द्वारा सुरक्षित भेजते हैं।",
        "safety_tip1": "<b>1. RBI लाइसेंस जांचें:</b> केवल RBI पंजीकृत बैंकों या NBFC से ही ऋण लें। अनधिकृत मोबाइल ऐप से बचें।",
        "safety_tip2": "<b>2. अग्रिम शुल्क धोखाधड़ी से बचें:</b> असली बैंक कभी भी ऋण जारी करने के लिए पहले नकद या एडवांस फीस नहीं मांगते।",
        "safety_tip3": "<b>3. सीधा बैंक ट्रांसफर:</b> सुनिश्चित करें कि लोन समझौता सीधे आपके वेतन/बैंक खाते में ट्रांसफर दिखाता हो।",
        "safety_tip4": "<b>4. ओटीपी और पिन सुरक्षित रखें:</b> लोन एजेंट का दावा करने वाले किसी भी व्यक्ति के साथ बैंक पासवर्ड, ओटीपी या पिन साझा न करें।",

        # Chat Interface
        "chat_title": "💬 फाइनबडी से बातचीत करें",
        "chat_welcome": "नमस्ते! 👋 मैं फाइनबडी हूँ, आपका मित्रवत वित्तीय सलाहकार। मुझसे बचत, बजट, लोन, आपातकालीन फंड या दैनिक खर्चों के बारे में कुछ भी पूछें!",
        "chat_placeholder": "अपना प्रश्न या संदेश यहाँ लिखें...",
        "quick_questions": "💡 तुरंत पूछें:",
        "q1": "मुझे हर महीने अपनी सैलरी का बंटवारा कैसे करना चाहिए?",
        "q2": "क्या स्मार्टफोन खरीदने के लिए पर्सनल लोन लेना सुरक्षित है?",
        "q3": "मैं जल्दी से इमरजेंसी फंड कैसे बना सकता हूँ?",
        "q4": "मैं सुरक्षित रूप से कितनी ईएमआई दे सकता हूँ?",

        # PDF Report
        "report_title": "📄 अपनी व्यक्तिगत वित्तीय रिपोर्ट डाउनलोड करें",
        "report_desc": "मनी हेल्थ स्कोर, बजट आवंटन, बचत योजना, लोन विश्लेषण और सलाहकार युक्तियों का संपूर्ण पीडीएफ सारांश प्राप्त करें।",
        "generate_pdf_btn": "📥 पीडीएफ रिपोर्ट जनरेट और डाउनलोड करें",
        "pdf_success": "✅ आपकी पीडीएफ रिपोर्ट जनरेट हो गई है!",

        # General Buttons & Words
        "currency_symbol": "₹",
        "months_unit": "महीने",
        "years_unit": "वर्ष",
        "per_month": "/माह"
    },

    "Marathi": {
        # App Header & Navigation
        "app_title": "फाइनबडी (FineBuddy)",
        "app_tagline": "तुमचा हुशार आणि विश्वासू वैयक्तिक वित्त सल्लागार",
        "lang_select": "🌐 भाषा निवडा",
        "nav_chat": "💬 एआय आर्थिक सल्लागार",
        "nav_budget": "📊 बजेट आणि हेल्थ स्कोर",
        "nav_savings": "🎯 बचत आणि व्हॉट-इफ",
        "nav_emi_loan": "🧮 ईएमआय आणि सुरक्षित कर्जे",
        "nav_report": "📄 रिपोर्ट डाउनलोड करा",

        # Profile Sidebar
        "profile_title": "👤 वापरकर्ता आर्थिक प्रोफाईल",
        "profile_subtitle": "अचूक सल्ल्यासाठी तुमची माहिती अद्ययावत ठेवा",
        "monthly_income": "मासिक उत्पन्न (₹)",
        "monthly_expenses": "मासिक खर्च (₹)",
        "age": "वय (वर्षे)",
        "city": "शहर / ठिकाण",
        "financial_goal": "मुख्य आर्थिक ध्येय",
        "save_profile": "💾 माहिती जतन करा",
        "profile_saved": "✅ प्रोफाईल यशस्वीरीत्या जतन झाली!",
        "profile_summary": "प्रोफाईल सारांश",
        "income_lbl": "उत्पन्न",
        "expense_lbl": "खर्च",
        "savings_lbl": "मासिक बचत (शिल्लक)",

        # Health Score
        "health_score_title": "मनी हेल्थ स्कोर (Money Health Score)",
        "health_score_desc": "तुमचा बचत दर, उत्पन्न-खर्च समतोल आणि आर्थिक सुरक्षितता यावर आधारित गणना केली आहे.",
        "score_label": "आर्थिक आरोग्य निर्देशांक",
        "status_excellent": "🌟 उत्कृष्ट आर्थिक स्थिती!",
        "status_good": "👍 चांगली आणि स्थिर स्थिती",
        "status_average": "⚠️ लक्ष देणे गरजेचे",
        "status_critical": "🚨 तातडीने सुधारणा आवश्यक!",
        "tip_title": "💡 स्कोर वाढवण्यासाठी सल्ला",

        # Goals Options
        "goal_emergency": "आणीबाणी निधी (Emergency Fund) तयार करणे",
        "goal_bike": "बाईक / स्कूटर खरेदी करणे",
        "goal_gadget": "फोन / लॅपटॉप खरेदी करणे",
        "goal_home": "घराच्या डाऊन पेमेंटसाठी बचत",
        "goal_education": "उच्च शिक्षण (Higher Education)",
        "goal_retirement": "दीर्घकालीन निवृत्ती (Retirement)",
        "goal_debt_free": "कर्जमुक्त (Debt-Free) होणे",

        # Budget Maker
        "budget_title": "📊 वैयक्तिक बजेट मेकर",
        "budget_desc": "तुमच्या उत्पन्नानुसार ५०/३०/२० नियमावर आधारित योग्य विभागणी.",
        "needs_label": "गरजा (भाडे, किराणा, बिले, औषधे - ५०%)",
        "wants_label": "इच्छा (बाहेर जेवणे, खरेदी, चित्रपट - ३०%)",
        "savings_invest_label": "बचत आणि गुंतवणूक (२०%)",
        "actual_spending": "तुमचा सध्याचा खर्च",
        "recommended_spending": "शिफारस केलेली ५०/३०/२० योजना",
        "category_breakdown": "तपशीलवार खर्च विभागणी",
        "rent_housing": "घरभाडे / निवारा",
        "food_groceries": "अन्न व किराणा",
        "utilities_bills": "वीज, पाणी व बिले",
        "transport": "वाहतूक / पेट्रोल",
        "entertainment": "मनोरंजन व लाईफस्टाईल",
        "misc": "इतर खर्च",
        "budget_analysis": "स्मार्ट बजेट सल्ला",

        # Savings & What-If
        "savings_title": "🎯 बचत ध्येय ट्रॅकर",
        "savings_desc": "तुमची ध्येये निश्चित करा आणि स्वप्ने किती लवकर पूर्ण होऊ शकतात ते पहा.",
        "target_amount": "ध्येय रक्कम (₹)",
        "current_saved": "आत्तापर्यंत झालेली बचत (₹)",
        "target_months": "कालावधी (महिने)",
        "monthly_req": "आवश्यक मासिक बचत",
        "available_surplus": "तुमची सध्याची मासिक बचत",
        "goal_achievable": "🎉 खूप छान! तुमची सध्याची बचत हे ध्येय सहज पूर्ण करू शकते.",
        "goal_tight": "⚠️ ध्येय गाठता येईल, पण दरमहा थोडे जास्त वाचवावे लागेल.",
        "goal_overbudget": "🚨 आवश्यक मासिक बचत तुमच्या सध्याच्या शिल्लक उत्पन्नापेक्षा जास्त आहे. कालावधी वाढवण्याचा विचार करा.",
        "what_if_title": "🔮 'व्हॉट-इफ' (What-If) विश्लेषण",
        "what_if_desc": "दरमहा थोडी अतिरिक्त बचत तुमचे ध्येय किती लवकर पूर्ण करते ते पहा!",
        "extra_save_label": "तुम्ही दरमहा अतिरिक्त रक्कम वाचवल्यास: (₹)",
        "what_if_result_months": "ध्येय गाठण्यासाठी लागणारे महिने",
        "what_if_interest_growth": "८% वार्षिक व्याजाने अंदाजित संपत्ती वाढ",

        # EMI & Safe Loans
        "emi_title": "🧮 ईएमआय कॅल्क्युलेटर आणि कर्ज सुरक्षा तपासणी",
        "loan_amount_label": "कर्ज रक्कम (₹)",
        "interest_rate_label": "वार्षिक व्याज दर (%)",
        "tenure_label": "कर्ज कालावधी (वर्षे)",
        "calculate_emi_btn": "ईएमआय शोधा",
        "monthly_emi_result": "दरमहा ईएमआय",
        "total_interest_result": "एकूण द्यायचे व्याज",
        "total_payment_result": "एकूण परतफेड",
        "emi_affordability": "ईएमआय परवडण्याची क्षमता (Affordability)",
        "safe_emi": "✅ सुरक्षित ईएमआय: उत्पन्नाच्या ३५% पेक्षा कमी. सहज परवडण्याजोगा!",
        "moderate_emi": "⚠️ मध्यम ईएमआय: उत्पन्नाच्या ३५-५०%. इतर खर्चावर लक्ष ठेवा.",
        "risky_emi": "🚨 धोकादायक ईएमआय: उत्पन्नाच्या ५०% पेक्षा जास्त. अजिबात शिफारस नाही!",
        
        "loan_recommend_title": "🏦 स्मार्ट कर्ज शिफारस प्रणाली",
        "loan_purpose_label": "कर्जाचा हेतू / गरज निवडा",
        "recommend_btn": "कर्ज सल्ला मिळवा",
        "max_safe_loan": "तुमच्या उत्पन्नानुसार कमाल सुरक्षित कर्ज मर्यादा",
        "rec_loan_type": "शिफारस केलेला कर्जाचा प्रकार",
        "rec_interest": "साधारण व्याज दर मर्यादा",
        
        # Loan Safety & Bank Transfer
        "loan_safety_header": "🛡️ बँक ट्रान्सफर सुरक्षितता आणि फसवणूक टाळण्याचे नियम",
        "bank_transfer_safe": "कर्जाची रक्कम तुमच्या बँक खात्यात सुरक्षितपणे जमा होते का?",
        "bank_transfer_answer": "होय! आरबीआय (RBI) मान्यताप्राप्त बँका आणि NBFC मंजूर केलेली कर्जाची रक्कम NEFT/RTGS/IMPS द्वारे थेट तुमच्या बँक खात्यात सुरक्षित जमा करतात.",
        "safety_tip1": "<b>1. RBI परवाना तपासा:</b> फक्त RBI नोंदणीकृत बँका किंवा NBFC कडूनच कर्ज घ्या. बेकायदेशीर मोबाईल ॲप्स टाळा.",
        "safety_tip2": "<b>2. ॲडव्हान्स फी फसवणूक टाळा:</b> खऱ्या बँका कर्ज मंजुरीसाठी आधी कधीही पैसे किंवा फी मागत नाहीत.",
        "safety_tip3": "<b>3. थेट बँक वर्ग:</b> कर्ज करारात रक्कम थेट तुमच्या पगाराच्या/बँक खात्यात जमा होत असल्याची खात्री करा.",
        "safety_tip4": "<b>4. ओटीपी आणि पिन सुरक्षित ठेवा:</b> कोणत्याही एजंटला तुमचा बँक पासवर्ड, ओटीपी किंवा पिन सांगू नका.",

        # Chat Interface
        "chat_title": "💬 फाइनबडीशी संवाद साधा",
        "chat_welcome": "नमस्कार! 👋 मी फाइनबडी, तुमचा वैयक्तिक वित्त सल्लागार. बचत, बजेट, कर्ज, आणीबाणी निधी किंवा रोजच्या खर्चाबाबत काहीही विचारा!",
        "chat_placeholder": "तुमचा प्रश्न किंवा संदेश येथे लिहा...",
        "quick_questions": "💡 त्वरित विचारा:",
        "q1": "दरमहा पगाराचे विभाजन कसे करावे?",
        "q2": "स्मार्टफोनसाठी पर्सनल लोन घेणे सुरक्षित आहे का?",
        "q3": "आणीबाणी निधी (Emergency Fund) जलद कसा बनवावा?",
        "q4": "मी किती ईएमआय सुरक्षितपणे भरू शकतो?",

        # PDF Report
        "report_title": "📄 तुमचा वैयक्तिक आर्थिक रिपोर्ट डाउनलोड करा",
        "report_desc": "मनी हेल्थ स्कोर, बजेट विभागणी, बचत योजना, कर्ज विश्लेषण आणि मार्गदर्शक सल्ल्याचा संपूर्ण पीडीएफ रिपोर्ट मिळवा.",
        "generate_pdf_btn": "📥 पीडीएफ रिपोर्ट जनरेट आणि डाउनलोड करा",
        "pdf_success": "✅ तुमचा पीडीएफ रिपोर्ट जनरेट झाला आहे!",

        # General Buttons & Words
        "currency_symbol": "₹",
        "months_unit": "महिने",
        "years_unit": "वर्षे",
        "per_month": "/महिना"
    }
}

def get_text(key: str, lang: str = "English") -> str:
    """Safely fetch translated text by key and language, defaulting to English if missing."""
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS["English"])
    return lang_dict.get(key, TRANSLATIONS["English"].get(key, key))
