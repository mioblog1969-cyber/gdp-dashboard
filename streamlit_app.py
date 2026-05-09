import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="NEXUS MARTUCCI V6 PRO", page_icon="🛡️")
st.title("🛡️ NEXUS MARTUCCI V6 PRO")

# Inserimento chiave (assicurati che sia corretta)
api_key = "AIzaSyCMPB2xUonWMcTACxLjhCH3Ig2_3AY15W8"
genai.configure(api_key=api_key)

# Usiamo il percorso assoluto del modello
try:
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error(f"Errore configurazione modello: {e}")

user_input = st.text_area("Cosa vuoi analizzare?")

if st.button("ESEGUI ANALISI"):
    if user_input:
        try:
            # Specifichiamo il metodo di generazione
            response = model.generate_content(user_input)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Dettaglio tecnico: {e}")
            st.info("Se l'errore persiste, prova a usare: 'gemini-pro' invece di 'gemini-1.5-flash' nel codice.")
