def classifica_studenti():
    studenti = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"]
    voti = [28, 15, 30, 22, 30, 18, 25, 29]
    
    print("=== SISTEMA DI CLASSIFICAZIONE STUDENTI ===\n")
    
    # 1: stampa lista completa con enumerate
    # formato: "1. Alice = 28/30"
    # gli studenti con voto 30 devono essere evidenziati con "⭐30⭐"
    # gli studenti bocciati (voto < 18) devono essere evidenziati con "❌BOCCIATO❌"
    
    print("Classifica completa:")
    for i, (studente, voto) in enumerate(zip(studenti, voti), start=1):
        if voto == 30:
            print(f"{i}. {studente} = ⭐{voto}⭐")
        elif voto < 18:
            print(f"{i}. {studente} = ❌BOCCIATO❌")
        else:
            print(f"{i}. {studente} = {voto}/30")
            
    # 2: crea liste separate con list comprehension
    # a) studenti promossi (voto >= 18)
    promossi = [s for s, v in zip(studenti, voti) if v >= 18]
    voti_promossi = [v for v in voti if v >= 18]
    # b) studenti con 30
    studenti_30 = [s for s, v in zip(studenti, voti) if v == 30]
    # c) studenti bocciati (voto < 18)
    bocciati = [s for s, v in zip(studenti, voti) if v < 18]
    
    print(f"\nPromossi ({len(promossi)}): {promossi}")
    print(f"Con 30 ({len(studenti_30)}): {studenti_30}")
    print(f"Bocciati ({len(bocciati)}): {bocciati}")
    
    #3: calcola statistiche solo sui promossi
    if voti_promossi:
        media = sum(voti_promossi) / len(voti_promossi)
        voto_max = max(voti_promossi)
        voto_min = min(voti_promossi)
        # trova il nome dello studente col voto più alto
        # (usa index() sulla lista voti e poi indexa studenti)
        indice_migliore = voti.index(voto_max)
        studente_migliore = studenti[indice_migliore]
        print(f"\nStatistiche sui promossi:")
        print(f"Media: {media:.2f}")
        print(f"Voto massimo: {voto_max}")
        print(f"Voto minimo: {voto_min}")
        print(f"Studente con voto più alto: {studente_migliore}")
    
    # 4: classifica per faasce con un ciclo for
    # e if/elif/else - conta quanti studenti in ogni fascia
    n_eccellenti = 0
    n_buoni = 0
    n_sufficienti = 0
    n_bocciati = 0
    
    for voto in voti:
        if voto == 30:
            n_eccellenti += 1
        elif voto >= 24:
            n_buoni += 1
        elif voto >= 18:
            n_sufficienti += 1
        else:
            n_bocciati += 1
            
    print(f"\nClassificazione per fasce:")
    print(f"  🔵 Eccellenti (28-30): {n_eccellenti}")
    print(f"  🟢 Buoni      (24-27): {n_buoni}")
    print(f"  🟡 Sufficienti(18-23): {n_sufficienti}")
    print(f"  🔴 Bocciati   (< 18):  {n_bocciati}")
    
    # 5: costruisci la classifica finale
    # crea una lista di tuple (voto, nome), ordinala in modo decrescente,
    # poi stampa la classifica con posizione, nome e voto
    classifica = sorted(zip(voti, studenti), reverse=True)
    print("\nClassifica finale:")
    for pos, (voto, nome) in enumerate(classifica, start=1):
        # mostra medaglia per i primi 3
        if pos == 1:
            medaglia = "🥇"
        elif pos == 2:
            medaglia = "🥈"
        elif pos == 3:
            medaglia = "🥉"
        else:
            medaglia = "  "
        print(f"  {medaglia} {pos}. {nome:<10} {voto}/30")


if __name__ == "__main__":
    classifica_studenti()