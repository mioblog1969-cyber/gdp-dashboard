import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="NEXUS MARTUCCI V6 PRO", page_icon="🛡️")

st.title("🛡️ NEXUS MARTUCCI V6 PRO")

if "GEMINI_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    # USIAMO IL MODELLO LATEST CHE È IL PIÙ COMPATIBILE
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
else:
    st.error("Chiave mancante nei Secrets!")

user_input = st.text_area("Cosa vuoi analizzare?")

if st.button("ESEGUI ANALISI"):
    try:
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception as e:
        st.error(f"Errore: {e}")
        st.info("Prova a controllare se la tua API Key è attiva su Google AI Studio.")
