def rubrica():
    # La rubrica parte già con alcuni contatti
    contatti = {
        "Alice Rossi":  ("333-1234567", "alice@email.com"),
        "Bruno Verdi":  ("347-9876543", "bruno@email.com"),
        "Carla Neri":   ("366-1112233", "carla@email.com"),
    }

    # Scrivo il menu principale della rubrica
    while True:
        print("\n╔══════════════════════════════╗")
        print("║         RUBRICA              ║")
        print("╚══════════════════════════════╝")
        print("1. Cerca contatto")
        print("2. Aggiungi contatto")
        print("3. Modifica contatto")
        print("4. Elimina contatto")
        print("5. Mostra tutti")
        print("0. Esci")
        scelta = input("Scelta: ").strip()
        if scelta == "1":
            nome = input("Nome del contatto da cercare: ").strip()
            if nome in contatti:
                print(f"{nome}: Telefono: {contatti[nome][0]}, Email: {contatti[nome][1]}")
            else:
                print("Contatto non trovato.")
        elif scelta == "2":
            nome = input("Nome del nuovo contatto: ").strip()
            if nome in contatti:
                print("Contatto già esistente.")
            else:
                telefono = input("Telefono: ").strip()
                email = input("Email: ").strip()
                contatti[nome] = (telefono, email)
                print("Contatto aggiunto.")
        elif scelta == "3":
            nome = input("Nome del contatto da modificare: ").strip()
            if nome in contatti:
                telefono = input(f"Nuovo telefono (attuale: {contatti[nome][0]}): ").strip()
                email = input(f"Nuova email (attuale: {contatti[nome][1]}): ").strip()
                contatti[nome] = (telefono, email)
                print("Contatto modificato.")
            else:
                print("Contatto non trovato.")
        elif scelta == "4":
            nome = input("Nome del contatto da eliminare: ").strip()
            if nome in contatti:
                del contatti[nome]
                print("Contatto eliminato.")
            else:
                print("Contatto non trovato.")
        elif scelta == "5":
            if contatti:
                for nome, info in contatti.items():
                    print(f"{nome}: Telefono: {info[0]}, Email: {info[1]}")
            else:
                print("La rubrica è vuota.")
        elif scelta == "0":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    rubrica()