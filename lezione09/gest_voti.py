# Raccogliere, gestire analizzare e creare un report di voti scolastici

def gestione_voti():
    
    voti = []
    print("=== REGISTRO VOTI ===")
    print("Inserisci i voti (18-30). Digita 'fine' per terminare.\n")
    
    # While e break per raccogliere i voti
    while True:
        testo = input("Inserisci un voto: ").strip()
        if testo.lower() == 'fine':
            print("Raccolta voti terminata.\n")
            break
        if not testo.isdigit():
            print("Input non valido. Inserisci un numero o 'fine'.")
            continue 
        
        voto = int(testo)
        
        if not (18 <= voto <= 30):
            print("Voto non valido. Inserisci un numero tra 18 e 30.")
            continue
        
        voti.append(voto)
        print(f" ✓ Aggiunto. Totale: {len(voti)} voti")
        
    # Nessun voto inserito
    if not voti:
        return
    
        # ── Analisi con cicli e condizioni ─────────────────
    somma = 0
    n_lode = 0
    n_eccellenti = 0   # 28-30
    n_buoni = 0        # 24-27
    n_sufficienti = 0  # 18-23

    for voto in voti:
        somma += voto
        if voto == 30:
            n_lode += 1      # potenziali lodi (non gestite qui)
        if voto >= 28:
            n_eccellenti += 1
        elif voto >= 24:
            n_buoni += 1
        else:
            n_sufficienti += 1

    media = somma / len(voti)

    # ── List comprehension per filtrare ────────────────
    voti_ordinati = sorted(voti)
    sopra_media = [v for v in voti if v >= media]
    trenta = [v for v in voti if v == 30]

    # ── Report ─────────────────────────────────────────
    print(f"\n{'='*40}")
    print(f"  REPORT VOTI ({len(voti)} esami)")
    print(f"{'='*40}")
    print(f"  Media: {media:.2f}/30")
    print(f"  Voto più alto: {max(voti)}")
    print(f"  Voto più basso: {min(voti)}")
    print(f"  Trenta:  {len(trenta)}")
    print(f"  Sopra media: {len(sopra_media)}/{len(voti)}")
    print(f"\n  Distribuzione:")
    print(f"  Eccellenti (28-30): {n_eccellenti}")
    print(f"  Buoni      (24-27): {n_buoni}")
    print(f"  Sufficienti(18-23): {n_sufficienti}")
    print(f"\n  Voti in ordine crescente:")
    print(f"  {voti_ordinati}")


if __name__ == "__main__":
    gestione_voti()