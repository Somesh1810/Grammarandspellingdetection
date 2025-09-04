import streamlit as st
import language_tool_python

st.title("Improved Grammar and Spelling Checker (LanguageTool)")

input_text = st.text_area("Enter your text:", height=200)

tool = language_tool_python.LanguageTool('en-US')

if st.button("Correct Grammar"):
    if input_text.strip() == "":
        st.warning("Please enter some text to correct.")
    else:
        # Check text with LanguageTool
        matches = tool.check(input_text)
        
        # Apply corrections
        corrected = language_tool_python.utils.correct(input_text, matches)
        
        st.success("✅ Grammar and spelling corrected.")
        st.text_area("Corrected Text:", value=corrected, height=200)
