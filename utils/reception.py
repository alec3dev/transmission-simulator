
import numpy as np

def demodulation(signal, type_demod):
    """Démodule le signal reçu"""
    if type_demod == "Cohérente":
        return signal  # Simplification
    # Implémenter d'autres méthodes...

def filtre_reception(signal, type_filtre):
    """Applique le filtre de réception"""
    if type_filtre == "Adapté":
        return signal  # Simplification
    # Implémenter d'autres filtres...

def recuperation_horloge(signal, methode):
    """Récupère l'horloge à partir du signal"""
    return np.arange(5, len(signal), 10)  # Simplification

def decision(signal, horloge, seuil):
    # Prendre le 1er échantillon de chaque bit Manchester
    echantillons = signal[horloge[::2]]  # [::2] pour sauter la 2ème moitié
    return [1 if e > seuil else 0 for e in echantillons]
