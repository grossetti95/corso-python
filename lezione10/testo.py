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

    # Il dizionario ha forma {parola: conteggio}
    frequenze = {}

    for parola in parole:
        if parola in frequenze:
            # la parola esiste già: incrementa il contatore
            frequenze[parola] += 1
        else:
            # la parola è nuova: inizializzala a 1
            frequenze[parola] = 1

    # Alternativa più compatta (equivalente):
    # frequenze[parola] = frequenze.get(parola, 0) + 1

      # sorted() su .items() restituisce lista di tuple (parola, conteggio)
    # key=lambda x: x[1] ordina per il secondo elemento della tupla (il conteggio)
    per_frequenza = sorted(frequenze.items(), key=lambda x: x[1], reverse=True)
    top5 = per_frequenza[:5]

    parole_uniche = set(parole)

    # Parole di stopword (da escludere dall'analisi semantica)
    stopwords = {"il", "lo", "la", "i", "gli", "le", "un", "una",
                 "di", "da", "in", "con", "su", "per", "tra", "fra",
                 "e", "o", "ma", "se", "che", "non", "è", "a", "del",
                 "della", "dei", "degli", "delle", "al", "alla"}

    # Parole significative = parole uniche - stopwords
    parole_significative = parole_uniche - stopwords

    print(f"\n{'='*45}")
    print(f"  REPORT ANALISI TESTO")
    print(f"{'='*45}")
    print(f"  Caratteri totali:      {len(testo)}")
    print(f"  Parole totali:         {len(parole)}")
    print(f"  Parole uniche:         {len(parole_uniche)}")
    print(f"  Parole significative:  {len(parole_significative)}")
    print(f"  Parole solo una volta: "
          f"{sum(1 for v in frequenze.values() if v == 1)}")

    print(f"\n  Top 5 parole più usate:")
    for parola, conteggio in top5:
        barra = "█" * conteggio
        print(f"  {parola:<15} {conteggio:3}x  {barra}")

    print(f"\n  Parole significative (ordinate):")
    print(f"  {', '.join(sorted(parole_significative))}")


if __name__ == "__main__":
    analisi_testo()