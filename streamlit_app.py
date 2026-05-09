import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="NEXUS MARTUCCI V6 PRO", page_icon="🛡️")
st.title("🛡️ NEXUS MARTUCCI V6 PRO")

# Usiamo la tua chiave che abbiamo verificato
api_key = "AIzaSyCMPB2xUonWMcTACxLjhCH3Ig2_3AY15W8"
genai.configure(api_key=api_key)

# CAMBIAMO MODELLO: Usiamo gemini-pro per massima compatibilità
try:
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Errore configurazione: {e}")

user_input = st.text_area("Cosa vuoi analizzare?")

if st.button("ESEGUI ANALISI"):
    if user_input:
        try:
            with st.spinner("Accesso ai database Pro..."):
                response = model.generate_content(user_input)
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Dettaglio tecnico: {e}")
            st.info("Se vedi ancora 404, Google sta impiegando più tempo del previsto ad attivare la tua chiave.")
    else:
        st.warning("Inserisci un testo.")
