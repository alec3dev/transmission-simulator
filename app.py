import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from utils.emission import codage_ligne, filtre_emission
from utils.canal import ajout_bruit
from utils.reception import demodulation, filtre_reception, recuperation_horloge, decision
from utils.visualisation import plot_signals

st.set_page_config(page_title="Simulateur de Transmission Numérique", layout="wide")
st.title("📡 Simulateur de Transmission Numérique")
st.sidebar.header("Paramètres de Simulation")

try:
    with st.expander("🎯 Côté Émetteur", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            bits_utilisateur = st.text_input("Entrez une séquence binaire (10 bits)", "1010010110")
            if len(bits_utilisateur) != 10 or not all(c in '01' for c in bits_utilisateur):
                st.error("Veuillez entrer exactement 10 bits (0 ou 1)")
                st.stop()
            bits_emis = [int(b) for b in bits_utilisateur]
        with col2:
            code_ligne = st.selectbox("Type de codage en ligne", ["NRZ", "Manchester", "Miller", "RZ"])
            type_filtre_emission = st.selectbox("Filtre d'émission", ["Rectangulaire", "Cosinus surélevé", "Gaussien"])

    with st.expander("🌐 Canal de Propagation", expanded=True):
        snr_db = st.slider("Rapport Signal/Bruit (dB)", -10, 30, 10)

    with st.expander("📥 Côté Récepteur", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            type_demodulation = st.selectbox("Type de démodulation", ["Cohérente", "Non cohérente"])
            type_filtre_reception = st.selectbox("Filtre de réception", ["Adapté", "Cosinus surélevé", "Gaussien"])
        with col2:
            methode_recup_horloge = st.sele
