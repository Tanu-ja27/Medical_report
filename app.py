
import streamlit as st
from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="t5-base")

# App title
st.set_page_config(page_title="Medical Report Summarizer")
st.title("🧠 NLP-Based Medical Report Summarizer")

# Text input
user_input = st.text_area("📋 Paste a medical report here:", height=200)

if st.button("Generate Summary"):
    if user_input.strip() != "":
        with st.spinner("Summarizing..."):
            summary = summarizer(user_input, max_length=50, min_length=10, do_sample=False)
            st.subheader("📝 Summary:")
            st.success(summary[0]['summary_text'])
    else:
        st.warning("Please paste a report to summarize.")
