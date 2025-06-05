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

# Fonction utilitaire pour affichage horizontal des séquences
def afficher_sequence(label, bits):
    texte = " ".join([f"{i}:{bit}" for i, bit in enumerate(bits)])
    st.write(f"**{label}** {texte}")

try:
    # 🎯 Émetteur
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

    # 🌐 Canal
    with st.expander("🌐 Canal de Propagation", expanded=True):
        snr_db = st.slider("Rapport Signal/Bruit (dB)", -10, 30, 10)

    # 📥 Récepteur
    with st.expander("📥 Côté Récepteur", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            type_demodulation = st.selectbox("Type de démodulation", ["Cohérente", "Non cohérente"])
            type_filtre_reception = st.selectbox("Filtre de réception", ["Adapté", "Cosinus surélevé", "Gaussien"])
        with col2:
            methode_recup_horloge = st.selectbox("Méthode de récupération d'horloge", ["Boucle à verrouillage de phase", "Dérivation"])
            seuil_decision = st.slider("Seuil de décision", 0.0, 1.0, 0.5, 0.01)

    # 🧪 Simulation
    if st.button("Lancer la Simulation"):
        try:
            signal_code = codage_ligne(bits_emis, code_ligne)
            signal_filtre = filtre_emission(signal_code, type_filtre_emission)
            signal_bruite = ajout_bruit(signal_filtre, snr_db)
            signal_demodule = demodulation(signal_bruite, type_demodulation)
            signal_filtre_reception = filtre_reception(signal_demodule, type_filtre_reception)
            horloge = recuperation_horloge(signal_filtre_reception, methode_recup_horloge)
            bits_recus = decision(signal_filtre_reception, horloge, seuil_decision)

            st.subheader("Résultats de la Simulation")
            col1, col2 = st.columns(2)

            with col1:
                afficher_sequence("🔹 Séquence émise :", bits_emis)
                afficher_sequence("🔸 Séquence reçue :", bits_recus)

                nb_erreurs = sum(b1 != b2 for b1, b2 in zip(bits_emis, bits_recus))
                if len(bits_recus) < len(bits_emis):
                    st.warning("⚠️ Séquence reçue incomplète.")
                elif nb_erreurs == 0:
                    st.success("✅ Transmission réussie sans erreurs !")
                else:
                    st.error(f"❌ Erreurs de transmission ({nb_erreurs} erreurs)")

            with col2:
                fig = plot_signals(bits_emis, signal_code, signal_filtre, signal_bruite,
                                   signal_demodule, signal_filtre_reception, bits_recus)
                st.pyplot(fig)

        except Exception as e:
            st.error(f"Erreur pendant la simulation : {e}")

except Exception as e:
    st.error(f"Erreur d'initialisation : {e}")

# Pied de page
st.markdown("""
---
🔗 [Code source sur GitHub](https://github.com/alec3dev/transmission-simulator)
""")
