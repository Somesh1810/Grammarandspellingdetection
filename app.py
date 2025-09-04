import streamlit as st
import requests

st.title("Improved Grammar and Spelling Checker (LanguageTool API)")

input_text = st.text_area("Enter your text:", height=200)

def correct_text(text):
    url = "https://api.languagetool.org/v2/check"
    data = {
        'text': text,
        'language': 'en-US',
    }
    response = requests.post(url, data=data)
    result = response.json()

    corrected_text = text
    # Apply corrections in reverse order to not mess up indices
    matches = result.get('matches', [])
    for match in reversed(matches):
        offset = match['offset']
        length = match['length']
        replacement = match['replacements'][0]['value'] if match['replacements'] else ''
        corrected_text = corrected_text[:offset] + replacement + corrected_text[offset+length:]
    return corrected_text

if st.button("Correct Grammar"):
    if input_text.strip() == "":
        st.warning("Please enter some text to correct.")
    else:
        corrected = correct_text(input_text)
        st.success("✅ Grammar and spelling corrected.")
        st.text_area("Corrected Text:", value=corrected, height=200)
