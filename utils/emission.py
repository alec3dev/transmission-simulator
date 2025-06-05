import numpy as np

def codage_ligne(bits, type_code):
    if type_code == "Manchester":
        manchester = []
        for bit in bits:
            manchester.extend([bit, 1-bit])
        return np.repeat(manchester, 5)
    elif type_code == "NRZ":
        return np.repeat(bits, 10)
    elif type_code == "Miller":
        # Implémentation simplifiée du codage Miller
        signal = []
        last = 1
        for bit in bits:
            if bit == 1:
                last = 1 - last
                signal.append(last)
            else:
                signal.append(last)
            signal.append(last)
        return np.repeat(signal, 5)
    elif type_code == "RZ":
        rz = []
        for bit in bits:
            rz.extend([bit, 0])
        return np.repeat(rz, 5)
    else:
        raise ValueError(f"Codage non supporté : {type_code}")

def filtre_emission(signal, type_filtre):
    if type_filtre == "Rectangulaire":
        return signal
    elif type_filtre == "Cosinus surélevé":
        return signal * np.hamming(len(signal))
    elif type_filtre == "Gaussien":
        gauss_filter = np.exp(-0.5 * ((np.arange(len(signal)) - len(signal)/2)/10)**2)
        gauss_filter /= np.max(gauss_filter)
        return signal * gauss_filter
    else:
        raise ValueError(f"Filtre d'émission non supporté : {type_filtre}")
