import numpy as np

def demodulation(signal, type_demod):
    if type_demod == "Cohérente":
        return signal
    elif type_demod == "Non cohérente":
        return np.abs(signal)
    else:
        raise ValueError(f"Démodulation non supportée : {type_demod}")

def filtre_reception(signal, type_filtre):
    if type_filtre == "Adapté":
        return signal
    elif type_filtre == "Cosinus surélevé":
        return signal * np.hamming(len(signal))
    elif type_filtre == "Gaussien":
        gauss_filter = np.exp(-0.5 * ((np.arange(len(signal)) - len(signal)/2)/10)**2)
        gauss_filter /= np.max(gauss_filter)
        return signal * gauss_filter
    else:
        raise ValueError(f"Filtre de réception non supporté : {type_filtre}")

def recuperation_horloge(signal, methode):
    if len(signal) < 10:
        raise ValueError("Signal trop court pour récupération d'horloge.")
    return np.arange(5, len(signal), 10)

def decision(signal, horloge, seuil):
    if max(horloge) >= len(signal):
        raise IndexError("Horloge dépasse la taille du signal.")
    echantillons = signal[horloge[::2]]
    return [1 if e > seuil else 0 for e in echantillons]
