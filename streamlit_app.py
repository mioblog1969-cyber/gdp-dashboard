import streamlit as st
import google.generativeai as genai

# 1. Configurazione della pagina
st.set_page_config(
    page_title="NEXUS MARTUCCI V6 PRO",
    page_icon="🛡️",
    layout="centered"
)

# 2. Stile grafico per rendere l'interfaccia professionale
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { 
        width: 100%; 
        border-radius: 10px; 
        height: 3.5em; 
        background-color: #007bff; 
        color: white; 
        font-weight: bold;
        border: none;
    }
    .stTextArea>div>div>textarea { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Titolo e Intestazione
st.title("🛡️ NEXUS MARTUCCI V6 PRO")
st.write("---")
st.info("Sistema di Intelligenza Artificiale pronto per l'analisi.")

# 4. Configurazione API Gemini
# Preleviamo la chiave dai Secrets di Streamlit
if "GEMINI_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    # Utilizziamo il modello 1.5-flash che è il più compatibile e veloce
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ ERRORE: Chiave API 'GEMINI_KEY' non trovata nei Secrets di Streamlit.")
    st.stop()

# 5. Area di Input
user_input = st.text_area("Inserisci la tua domanda o il testo da analizzare:", height=150, placeholder="Esempio: Analizza i rischi cyber per la mia azienda...")

# 6. Logica di Esecuzione
if st.button("ESEGUI ANALISI"):
    if user_input:
        try:
            with st.spinner("Nexus sta elaborando il responso..."):
                # Generazione della risposta
                response = model.generate_content(user_input)
                
                st.write("---")
                st.subheader("🤖 Responso del Nexus:")
                st.markdown(response.text)
                st.success("Analisi completata con successo.")
        except Exception as e:
            # Gestione errori migliorata per darti suggerimenti chiari
            st.error(f"Si è verificato un errore durante l'analisi.")
            st.warning(f"Dettaglio tecnico: {e}")
            if "404" in str(e):
                st.info("Consiglio: Se l'errore è 404, prova a generare una NUOVA chiave API su Google AI Studio.")
    else:
        st.warning("Per favore, inserisci un testo prima di cliccare su Esegui.")

# 7. Footer
st.write("---")
st.caption("Nexus Martucci V6 Pro | Protetto da crittografia end-to-end")
