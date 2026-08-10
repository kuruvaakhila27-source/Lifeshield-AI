import streamlit as st
import re

st.set_page_config(page_title="LifeShield AI", page_icon="🛡️")

st.title("🛡️ LifeShield AI")
st.write("Suspicious SMS, WhatsApp message, email, or link ni paste cheyyi.")

message = st.text_area("📩 Enter Message")

keywords = [
    "otp", "password", "urgent", "click here",
    "winner", "won", "lottery", "prize",
    "bank", "account blocked", "verify", "payment",
    "upi", "pin"
]

if st.button("🔍 Analyze"):

    text = message.lower()
    score = 0
    reasons = []

    # keyword check
    for k in keywords:
        if k in text:
            score += 10
            reasons.append(k)

    # URL check
    if re.search(r"https?://|www\.", text):
        score += 20
        reasons.append("suspicious link")

    # Money check
    if re.search(r"₹\s?\d+|\$\s?\d+|\d+\s?(lakh|lakhs|crore|crores)", text):
        score += 15
        reasons.append("money mentioned")

    score = min(score, 100)

    st.subheader("🧠 Analysis Result")

    if score >= 50:
        st.error(f"🔴 HIGH RISK ({score}/100)")
    elif score >= 25:
        st.warning(f"🟠 MEDIUM RISK ({score}/100)")
    else:
        st.success(f"🟢 LOW RISK ({score}/100)")

    st.subheader("⚠️ Detected Indicators")

    if reasons:
        for r in reasons:
            st.write("•", r)
    else:
        st.write("No suspicious indicators found.")

    st.subheader("🛡️ Safety Advice")
    st.info("OTP, PIN, password, bank details evariki cheppaku. Suspicious links click cheyyaku.")