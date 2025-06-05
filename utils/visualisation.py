import matplotlib.pyplot as plt

def plot_signals(bits_emis, signal_code, signal_filtre, signal_bruite,
                 signal_demodule, signal_filtre_reception, bits_recus):
    fig, axes = plt.subplots(4, 1, figsize=(12, 8))

    axes[0].plot(signal_code, label="Signal codé")
    axes[0].plot(signal_filtre, label="Signal filtré")
    axes[0].set_title("Côté Émetteur")
    axes[0].legend()

    axes[1].plot(signal_bruite, label="Signal bruité")
    axes[1].set_title("Canal Bruité")
    axes[1].legend()

    axes[2].plot(signal_demodule, label="Signal démodulé")
    axes[2].plot(signal_filtre_reception, label="Signal filtré (réception)")
    axes[2].set_title("Côté Récepteur")
    axes[2].legend()

    axes[3].stem(bits_emis, linefmt='b-', markerfmt='bo', label="Émis")
    axes[3].stem(bits_recus, linefmt='r--', markerfmt='rx', label="Reçus")
    axes[3].set_title("Comparaison Bits Émis/Reçus")
    axes[3].legend()

    plt.tight_layout()
    return fig
