import streamlit as st
from textblob import TextBlob

st.title("Grammar and Spelling Checker (TextBlob)")

# Input text area
input_text = st.text_area("Enter your text:", height=200)

# Button to trigger correction
if st.button("Correct Grammar"):
    if input_text.strip() == "":
        st.warning("Please enter some text to correct.")
    else:
        blob = TextBlob(input_text)
        corrected = blob.correct()
        st.success("✅ Grammar and spelling corrected.")
        st.text_area("Corrected Text:", value=str(corrected), height=200)
