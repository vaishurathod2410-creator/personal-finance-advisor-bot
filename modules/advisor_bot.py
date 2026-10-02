"""
AI Financial Advisor Bot module with multi-language natural responses and session chat memory.
"""

import streamlit as st
from translations import get_text
from modules.user_profile import calculate_health_score

def init_chat_history(lang: str):
    """Initialize chat memory in st.session_state if empty."""
    if "chat_history" not in st.session_state or not st.session_state.chat_history:
        welcome_msg = get_text("chat_welcome", lang)
        st.session_state.chat_history = [
            {"role": "assistant", "content": welcome_msg}
        ]

def generate_financial_advice(user_prompt: str, lang: str) -> str:
    """
    Generate intelligent, contextual, multi-lingual advisor response based on user profile and query intent.
    """
    profile = st.session_state.user_profile
    income = profile.get("income", 50000.0)
    expenses = profile.get("expenses", 30000.0)
    surplus = max(0.0, income - expenses)
    age = profile.get("age", 28)
    goal = profile.get("goal", "Emergency Fund")
    health = calculate_health_score(income, expenses)

    prompt_lower = user_prompt.lower()

    # Rule-Based Intent Parser with Rich Multi-lingual Knowledge Base
    if any(w in prompt_lower for w in ["allocate", "salary", "budget", "50/30/20", "बंटवारा", "सैलरी", "बजेट", "विभाजन"]):
        if lang == "Hindi":
            return (
                f"अपनी ₹{income:,.0f} की मासिक आय के लिए 50/30/20 नियम सबसे बेहतरीन रहेगा:\n\n"
                f"1. **आवश्यकताएं (50% - ₹{income*0.5:,.0f}):** किराया, राशन, बिजली-पानी के बिल और दवाएं।\n"
                f"2. **इच्छाएं (30% - ₹{income*0.3:,.0f}):** बाहर खाना, शॉपिंग और मनोरंजन।\n"
                f"3. **बचत (20% - ₹{income*0.2:,.0f}):** आपातकालीन फंड और म्यूचुअल फंड/एसआईपी।\n\n"
                f"आपकी वर्तमान मासिक बचत ₹{surplus:,.0f} है। इसे हमेशा महीने की शुरुआत में ही अलग रख दें!"
            )
        elif lang == "Marathi":
            return (
                f"तुमच्या ₹{income:,.0f} मासिक उत्पन्नासाठी ५०/३०/२० नियम अतिशय उपयुक्त आहे:\n\n"
                f"1. **गरजा (५०% - ₹{income*0.5:,.0f}):** घरभाडे, किराणा, बिले आणि औषधे.\n"
                f"2. **इच्छा (३०% - ₹{income*0.3:,.0f}):** बाहेर जेवणे, खरेदी आणि मनोरंजन.\n"
                f"3. **बचत (२०% - ₹{income*0.2:,.0f}):** आणीबाणी निधी आणि म्युच्युअल फंड एसआयपी.\n\n"
                f"तुमची सध्याची मासिक बचत ₹{surplus:,.0f} आहे. ती नेहमी महिन्याच्या सुरुवातीलाच बाजूला ठेवा!"
            )
        else:
            return (
                f"For your monthly income of ₹{income:,.0f}, here is the ideal **50/30/20 Budget Plan**:\n\n"
                f"• **Needs (50% = ₹{income*0.5:,.0f}):** Rent, groceries, utility bills, and medical expenses.\n"
                f"• **Wants (30% = ₹{income*0.3:,.0f}):** Dining out, shopping, and entertainment.\n"
                f"• **Savings & Investments (20% = ₹{income*0.2:,.0f}):** Emergency fund and Mutual Fund SIPs.\n\n"
                f"Your current monthly surplus is **₹{surplus:,.0f}**. Set aside your savings on salary day before spending!"
            )

    elif any(w in prompt_lower for w in ["phone", "gadget", "personal loan", "स्मार्टफोन", "गैजेट", "पर्सनल लोन", "लॅपटॉप"]):
        if lang == "Hindi":
            return (
                "📱 **स्मार्टफोन/गैजेट के लिए लोन सलाह:**\n\n"
                "गैजेट्स की कीमत समय के साथ तेजी से घटती है। इसलिए:\n"
                "• पर्सनल लोन लेने से बचें क्योंकि ब्याज दर 12%-16% होती है जो महंगी पड़ती है।\n"
                "• यदि आवश्यक हो, तो केवल **नो-कॉस्ट ईएमआई (No-Cost EMI)** का विकल्प चुनें और सुनिश्चित करें कि ईएमआई आपकी आय के 15% से कम हो।\n"
                "• **सुरक्षा नियम:** लोन केवल पंजीकृत बैंकों से ही लें। किसी भी ऐप को पहले एडवांस फीस न दें और पैसे सीधे आपके बैंक अकाउंट में ही ट्रांसफर होने चाहिए।"
            )
        elif lang == "Marathi":
            return (
                "📱 **स्मार्टफोन/गॅझेटसाठी कर्ज सल्ला:**\n\n"
                "गॅझेट्सचे मूल्य वेगाने कमी होते. त्यामुळे:\n"
                "• पर्सनल लोन घेणे टाळा कारण त्याचा व्याज दर १२%-१६% असतो.\n"
                "• अत्यंत गरज असल्यास फक्त **नो-कॉस्ट ईएमआई (No-Cost EMI)** वापरा आणि ईएमआय उत्पन्नाच्या १५% पेक्षा जास्त नसावा.\n"
                "• **सुरक्षितता:** नेहमी आरबीआय नोंदणीकृत बँकेकडूनच ईएमआय घ्या. आधी कोणतीही फी देऊ नका आणि रक्कम थेट तुमच्या बँक खात्यात जमा झाली पाहिजे."
            )
        else:
            return (
                "📱 **Advice on Smartphone / Gadget Loans:**\n\n"
                "Depreciating assets like electronics should ideally be bought from savings rather than costly loans.\n"
                "• **Avoid High-Interest Personal Loans:** Rates can range between 12%-16% p.a.\n"
                "• **Opt for No-Cost EMI:** If urgent, choose a 3 to 6 month No-Cost EMI where total EMI is less than 15% of your monthly income.\n"
                "• **Bank Safety Tip:** Real lenders transfer approved loan amounts straight to your bank account with zero upfront fee."
            )

    elif any(w in prompt_lower for w in ["emergency", "fund", "आपातकालीन", "इमरजेंसी", "आणीबाणी"]):
        target_ef = expenses * 6
        months_to_save = target_ef / surplus if surplus > 0 else 99
        if lang == "Hindi":
            return (
                f"🛡️ **आपातकालीन फंड (Emergency Fund) योजना:**\n\n"
                f"आपके मासिक खर्च (₹{expenses:,.0f}) के अनुसार आपका 6 महीने का इमरजेंसी फंड **₹{target_ef:,.0f}** होना चाहिए।\n\n"
                f"• आपकी मासिक बचत ₹{surplus:,.0f} से आप इसे लगभग **{months_to_save:.1f} महीनों** में पूरा कर सकते हैं।\n"
                f"• इस पैसे को हाई-यिल्ड सेविंग्स अकाउंट या लिक्विड म्यूचुअल फंड में रखें ताकि जरूरत पड़ने पर तुरंत निकाला जा सके।"
            )
        elif lang == "Marathi":
            return (
                f"🛡️ **आणीबाणी निधी (Emergency Fund) योजना:**\n\n"
                f"तुमच्या मासिक खर्चाच्या (₹{expenses:,.0f}) आधारावर तुमचा ६ महिन्यांचा आणीबाणी निधी **₹{target_ef:,.0f}** असावा.\n\n"
                f"• तुमच्या मासिक बचतीतून (₹{surplus:,.0f}) तुम्ही हा निधी सुमारे **{months_to_save:.1f} महिन्यात** पूर्ण करू शकता.\n"
                f"• हे पैसे नेहमी बचत खात्यात किंवा लिक्विड फंडात ठेवा जेणेकरून संकटसमयी त्वरित मिळतील."
            )
        else:
            return (
                f"🛡️ **Building Your Emergency Fund:**\n\n"
                f"Based on your current monthly expenses (₹{expenses:,.0f}), your recommended 6-month safety buffer is **₹{target_ef:,.0f}**.\n\n"
                f"• Saving your monthly surplus of ₹{surplus:,.0f}, you will achieve this target in **{months_to_save:.1f} months**.\n"
                f"• Keep this emergency fund in a Liquid Mutual Fund or high-interest savings bank account for instant withdrawal."
            )

    elif any(w in prompt_lower for w in ["how much emi", "affordable", "safe loan", "ईएमआई", "सुरक्षित लोन", "कर्ज"]):
        max_safe_emi = income * 0.35
        if lang == "Hindi":
            return (
                f"💳 **सुरक्षित ईएमआई सीमा:**\n\n"
                f"आपकी ₹{income:,.0f} की आय के लिए, आपकी कुल मासिक ईएमआई **₹{max_safe_emi:,.0f}** (आय का 35%) से अधिक नहीं होनी चाहिए।\n\n"
                f"• यदि आपकी ईएमआई इससे ज्यादा होती है, तो दैनिक खर्चों में तंगी हो सकती है।\n"
                f"• **सुरक्षा जांच:** हमेशा सुनिश्चित करें कि लोन केवल स्वीकृत बैंकों से ही सीधे आपके वेतन खाते में ट्रांसफर हो।"
            )
        elif lang == "Marathi":
            return (
                f"💳 **सुरक्षित ईएमआय मर्यादा:**\n\n"
                f"तुमच्या ₹{income:,.0f} उत्पन्नासाठी, तुमची एकूण मासिक ईएमआय **₹{max_safe_emi:,.0f}** (उत्पन्नाच्या ३५%) पेक्षा जास्त नसावी.\n\n"
                f"• ईएमआय यापेक्षा जास्त असल्यास दैनंदिन खर्चात अडचण येऊ शकते.\n"
                f"• **सुरक्षितता:** कर्ज नेहमी आरबीआय नोंदणीकृत बँकेकडूनच थेट तुमच्या खात्यात जमा व्हावे."
            )
        else:
            return (
                f"💳 **Safe EMI Affordability Limit:**\n\n"
                f"For your monthly income of ₹{income:,.0f}, your total combined monthly EMIs should ideally remain under **₹{max_safe_emi:,.0f}** (35% of income).\n\n"
                f"• Keeping EMIs under this ceiling protects your monthly cash flow and keeps your Money Health Score high ({health['score']}/100).\n"
                f"• **Bank Safety:** Genuine lenders transfer funds directly into your verified bank account via NEFT/IMPS."
            )

    else:
        # Default AI companion reply incorporating Money Health Score & Profile
        if lang == "Hindi":
            return (
                f"धन्यवाद आपके प्रश्न के लिए! 😊\n\n"
                f"आपकी वर्तमान वित्तीय प्रोफ़ाइल के अनुसार:\n"
                f"• **आय:** ₹{income:,.0f} | **खर्च:** ₹{expenses:,.0f}\n"
                f"• **मनी हेल्थ स्कोर:** {health['score']}/100 ({get_text(health['status_key'], lang)})\n"
                f"• **प्राथमिक लक्ष्य:** {goal}\n\n"
                f"वित्तीय सफलता के लिए हमेशा अपनी बचत दर को 20% से ऊपर रखें और किसी भी गैर-जरूरी लोन से बचें। क्या आप बजट, बचत या लोन के बारे में और जानना चाहते हैं?"
            )
        elif lang == "Marathi":
            return (
                f"तुमच्या प्रश्नासाठी धन्यवाद! 😊\n\n"
                f"तुमच्या सध्याच्या आर्थिक माहितीनुसार:\n"
                f"• **उत्पन्न:** ₹{income:,.0f} | **खर्च:** ₹{expenses:,.0f}\n"
                f"• **मनी हेल्थ स्कोर:** {health['score']}/100 ({get_text(health['status_key'], lang)})\n"
                f"• **मुख्य ध्येय:** {goal}\n\n"
                f"आर्थिक स्थैर्यासाठी दरमहा २०% पेक्षा जास्त बचत करा आणि विनाकारण कर्ज घेणे टाळा. तुम्हाला बजेट किंवा कर्जाबाबत अधिक माहिती हवी आहे का?"
            )
        else:
            return (
                f"Thank you for asking! 😊\n\n"
                f"Based on your profile snapshot:\n"
                f"• **Monthly Income:** ₹{income:,.0f} | **Expenses:** ₹{expenses:,.0f}\n"
                f"• **Money Health Score:** {health['score']}/100 ({get_text(health['status_key'], lang)})\n"
                f"• **Primary Goal:** {goal}\n\n"
                f"To keep your finances healthy, aim to save at least 20% of your income each month. Feel free to ask me more specific questions about budgeting, savings, or EMI calculations!"
            )

def render_chat_interface(lang: str):
    """Render the main Chat UI with history and prompt chips."""
    init_chat_history(lang)

    st.markdown(f"## {get_text('chat_title', lang)}")
    st.caption(get_text("app_tagline", lang))

    # Display Chat History
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Quick Question Chips
    st.markdown(f"##### {get_text('quick_questions', lang)}")
    qc1, qc2, qc3, qc4 = st.columns(4)

    prompt_to_send = None

    if qc1.button(get_text("q1", lang), use_container_width=True):
        prompt_to_send = get_text("q1", lang)
    elif qc2.button(get_text("q2", lang), use_container_width=True):
        prompt_to_send = get_text("q2", lang)
    elif qc3.button(get_text("q3", lang), use_container_width=True):
        prompt_to_send = get_text("q3", lang)
    elif qc4.button(get_text("q4", lang), use_container_width=True):
        prompt_to_send = get_text("q4", lang)

    # Chat Input Box
    user_input = st.chat_input(get_text("chat_placeholder", lang))

    if user_input:
        prompt_to_send = user_input

    if prompt_to_send:
        # Append User Message
        st.session_state.chat_history.append({"role": "user", "content": prompt_to_send})
        
        # Generate Bot Response
        bot_reply = generate_financial_advice(prompt_to_send, lang)
        st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
        
        st.rerun()
