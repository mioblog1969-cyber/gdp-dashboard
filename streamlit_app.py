import streamlit as st
import google.generativeai as genai

# Configurazione della pagina
st.set_page_config(page_title="NEXUS MARTUCCI V6", page_icon="🛡️", layout="wide")

# Recupero della chiave segreta dai Secrets di Streamlit
try:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
except:
    st.error("Errore: Chiave API non trovata nei Secrets! Configura GEMINI_KEY su Streamlit Cloud.")

# Stile CSS per un look Cyberpunk/Professionale
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ffcc; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #00ffcc; color: black; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #1a1c23; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Header con lo Scudo
st.title("🛡️ NEXUS MARTUCCI V6 PRO")
st.subheader("Sistemi Avanzati di Analisi AI")
st.write("---")

# Layout a due colonne
col1, col2 = st.columns([1, 2])

with col1:
    st.sidebar.header("⚙️ PANNELLO DI CONTROLLO")
    tipo_analisi = st.sidebar.selectbox("Scegli Analisi", ["Analisi Tecnica", "Strategia Business", "Cyber Security", "Assistente Personale"])
    temperatura = st.sidebar.slider("Creatività AI", 0.0, 1.0, 0.7)

with col2:
    st.write(f"### 🚀 Modalità Attiva: {tipo_analisi}")
    user_input = st.text_area("Inserisci i dati o la domanda per l'analisi:", placeholder="Scrivi qui...")

    if st.button("ESEGUI ANALISI"):
        if user_input:
            with st.spinner("⚡ Elaborazione dati in corso..."):
                try:
                    model = genai.GenerativeModel("gemini-pro")
                    response = model.generate_content(f"Agisci come un esperto in {tipo_analisi}. Analizza quanto segue: {user_input}")
                    st.success("✅ Analisi Completata")
                    st.markdown("---")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Errore durante l'analisi: {e}")
        else:
            st.warning("⚠️ Inserisci un testo prima di procedere.")

st.write("---")
st.caption("Nexus Martucci V6.0 - Sistema Protetto e Crittografato")
