def analizza_temperature():
    # Lista di temperature settimanali (già fornita)
    temperature = [22.5, 19.0, 25.3, 28.1, 17.8, 23.6, 21.0]
    giorni = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]

    print("=== Analisi Temperature Settimanali ===\n")

    # PUNTO 1: stampa ogni giorno con la sua temperatura
    # usando zip() e un ciclo for
    # formato atteso: "Lun: 22.5°C"
    for giorno, temp in zip(giorni, temperature):        # usa zip()
        print(f"{giorno}: {temp}°C")               # completa la f-string

    # PUNTO 2: calcola la media con sum() e len()
    media = sum(temperature) / len(temperature)
    print(f"\nMedia settimanale: {media:.1f}°C")

    # PUNTO 3: trova i giorni sopra la media con una list comprehension
    # deve produrre: ["Gio"] (solo Gio supera la media)
    caldi = [giorni[i] for i, t in enumerate(temperature) if t > media]  # usa enumerate() e una list comprehension
    print(f"Giorni sopra la media: {caldi}")

    # PUNTO 4: ordina le temperature (copia — non modificare l'originale)
    # usa sorted() per non toccare la lista originale
    ordinate = sorted(temperature)
    print(f"Da più fredda a più calda: {ordinate}")

    # PUNTO 5: aggiungi una nuova temperatura per lunedì prossimo
    # (usa append) e stampa la lista aggiornata
    nuova_temp = float(input("\nTemperatura lunedì prossimo: "))
    temperature.append(nuova_temp)  # usa append()
    print(f"Lista aggiornata: {temperature}")


if __name__ == "__main__":
    analizza_temperature()