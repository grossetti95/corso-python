def analisi_testo():
    print("=== Analisi Testo ===")
    print("Inserisci il testo (riga vuota per terminare):\n")

    righe = []
    # usa while True + break per raccogliere righe finché l'utente
    # inserisce una riga vuota
    while True:
        riga = input()
        if riga == "":
            break
        righe.append(riga)

    testo = " ".join(righe)
    if not testo.strip():
        print("Nessun testo inserito.")
        return
    
        # Rimuovi i caratteri di punteggiatura dal testo
    # Caratteri da rimuovere
    punteggiatura = ".,;:!?()[]{}\"'-"
    testo_pulito = ""

    for c in testo:
        if c in punteggiatura:
            # sostituisci con uno spazio invece di rimuovere
            # così "ciao,mondo" diventa "ciao mondo" e non "ciaomondo"
            testo_pulito += " "
        else:
            testo_pulito += c

    # Lista di tutte le parole in minuscolo
    parole = [p.lower() for p in testo_pulito.split() if p]