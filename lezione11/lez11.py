def valida_e_formatta():
    print("--- Validatore dati anagrafici ---\n")
    dati = {}

    # Validazione nome
    while True:
        nome = input("Nome e cognome: ").strip()
        if not nome:
            print("Il nome non può essere vuoto. Riprova.")
            continue
        # Controlla che ogni carattere sia una lettera o uno spazio
        valido = True
        for c in nome:
            if not (c.isalpha() or c == " "):
                valido = False
                break
        if not valido:
            print("Il nome deve contenere solo lettere e spazi. Riprova.")
            continue

        # Normalizza: title case e rimuove spazi extra
        dati["nome"] = " ".join(nome.title().split())
        break

    # CODICE FISCALE: 16 CARATTERI ALFANUMERICI (tioni tiandri (rea) è un frocio di merda)

    while True:
        cf = input("Codice fiscale: ").strip().upper()
        if len(cf) != 16:
            print("Il codice fiscale deve essere di 16 caratteri. Riprova.")
            continue
        if not cf.isalnum():
            print("Il codice fiscale deve essere alfanumerico. Riprova.")
            continue
        dati["codice_fiscale"] = cf
        break

    # EMAIL: formato valido

    while True:
        email = input("Email: ").strip().lower()
        if not email:
            print("L'email non può essere vuota. Riprova.")
            continue
        if "@" not in email or "." not in email.split("@")[-1]:
            print("L'email non è valida. Riprova.")
            continue
        dati["email"] = email
        break

    # TELEFONO: 10 cifre numeriche

    while True:
        telefono = input("Telefono: ").strip()
        if len(telefono) != 10:
            print("Il telefono deve essere di 10 cifre. Riprova.")
            continue
        if not telefono.isdigit():
            print("Il telefono deve contenere solo cifre. Riprova.")
            continue
        dati["telefono"] = telefono
        break

    return dati