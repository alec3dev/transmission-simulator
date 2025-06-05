
import numpy as np

def codage_ligne(bits, type_code):
    if type_code == "Manchester":
        manchester = []
        for bit in bits:
            manchester.extend([bit, 1-bit])  # 1->[1,0], 0->[0,1]
        return np.repeat(manchester, 5)  # 10 échantillons/bit
    
def filtre_emission(signal, type_filtre):
    """Applique le filtre d'émission au signal"""
    if type_filtre == "Rectangulaire":
        return signal
    # Implémenter d'autres filtres...
