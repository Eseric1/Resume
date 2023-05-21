import base64
import streamlit as st

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        pdf_display = f'<iframe src="01-Erics-Resume.pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
        return pdf_display
    
st.markdown(show_pdf("01-Erics-Resume.pdf"), unsafe_allow_html=True)
