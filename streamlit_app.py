import streamlit as st
import google.generativeai as genai
import os

# Configurazione Pagina
st.set_page_config(page_title="NEXUS MARTUCCI V6 PRO", page_icon="🛡️", layout="wide")

# Stile Custom
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ NEXUS MARTUCCI V6 PRO")
st.write("Sistema di Analisi Avanzata Operativo.")

# Recupero Chiave dai Secrets
if "GEMINI_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
else:
    st.error("⚠️ Chiave API non trovata nei Secrets!")

# Selezione Modello Aggiornato
model = genai.GenerativeModel('gemini-1.5-flash')

# Interfaccia
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("Inserisci il testo per l'analisi:", placeholder="Scrivi qui...")
    if st.button("ESEGUI ANALISI"):
        if user_input:
            try:
                with st.spinner("Nexus sta elaborando..."):
                    response = model.generate_content(user_input)
                    st.subheader("Responso Nexus:")
                    st.write(response.text)
            except Exception as e:
                st.error(f"Errore durante l'analisi: {e}")
        else:
            st.warning("Inserisci un testo prima di procedere.")

with col2:
    st.info("📌 **Status Sistema:** Online\n\n**Livello Sicurezza:** Massimo\n\n**Motore:** Gemini 1.5 Flash")
