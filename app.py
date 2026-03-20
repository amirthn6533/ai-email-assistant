import streamlit as st
from ai.analyzer import analyze_email


st.set_page_config(page_title="AI Email Assistant", page_icon="📧")


st.markdown("<h1 style='text-align: center;'>📧 AI Email Assistant</h1>", unsafe_allow_html=True)

st.write("Analyze emails using AI — importance, summary, and reply")


email = st.text_area("✉️ Enter your email:", height=200)


if st.button("🚀 Analyze Email"):
    if email:
        with st.spinner("Analyzing... ⏳"):
            result = analyze_email(email)


        st.markdown("## 📊 Results")

        st.success("✅ Analysis completed")


        analysis = result["analysis"]

        st.markdown("### 🧠 Full Analysis")
        st.code(analysis)

    else:
        st.warning("⚠️ Please enter an email")