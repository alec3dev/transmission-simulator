import numpy as np

def ajout_bruit(signal, snr_db):
    """Ajoute un bruit gaussien au signal selon le SNR spécifié"""
    puissance_signal = np.mean(signal**2)
    puissance_bruit = puissance_signal / (10 ** (snr_db / 10))
    bruit = np.random.normal(0, np.sqrt(puissance_bruit), len(signal))
    return signal + bruit
