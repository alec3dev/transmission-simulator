import numpy as np

def ajout_bruit(signal, snr_db):
    if len(signal) == 0:
        raise ValueError("Signal vide, impossible d'ajouter du bruit.")
    puissance_signal = np.mean(np.square(signal))
    puissance_bruit = puissance_signal / (10 ** (snr_db / 10))
    bruit = np.random.normal(0, np.sqrt(puissance_bruit), len(signal))
    return signal + bruit
