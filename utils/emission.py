
import numpy as np

def codage_ligne(bits, type_code):
    """Convertit la séquence binaire en signal selon le codage en ligne spécifié"""
    if type_code == "NRZ":
        return np.repeat(bits, 10)  # 10 échantillons par bit
    elif type_code == "Manchester":
        manchester = []
        for bit in bits:
            manchester.extend([bit, 1-bit] * 5)
        return np.array(manchester)
    # Ajouter d'autres types de codage...
    
def filtre_emission(signal, type_filtre):
    """Applique le filtre d'émission au signal"""
    if type_filtre == "Rectangulaire":
        return signal
    # Implémenter d'autres filtres...
