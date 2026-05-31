# Lezione 5 — variabili, tipi, input e output

def presenta_utente():
    """Raccoglie le informazioni dell'utente e le presenta formattate."""

    print("=== Benvenuto nel tuo profilo ===\n")

    # Input e conversione dei tipi

    nome = input("Come ti chiami? ")
    eta = int(input("Quanti anni hai? "))
    altezza = float(input("Quanto sei alto/a? (es. 1.75) "))
    citta = input("In quale città abiti? ")

    # Calcoli

    anno_nascita = 2026 - eta
    eta_pensione = 67 - eta

    # Output formattato con f-string

    print("\n=== Il tuo profilo ===")
    print(f"Nome:          {nome}")
    print(f"Età:           {eta} anni")
    print(f"Altezza:       {altezza:.2f} m")
    print(f"Città:         {citta}")
    print(f"Anno nascita:  {anno_nascita}")
    print(f"Anni alla pensione: {eta_pensione}")

    # Verifica tipi
    
    print("\n=== Tipi delle variabili ===")
    print(f"nome è di tipo:    {type(nome)}")
    print(f"eta è di tipo:     {type(eta)}")
    print(f"altezza è di tipo: {type(altezza)}")


if __name__ == "__main__":
    presenta_utente()