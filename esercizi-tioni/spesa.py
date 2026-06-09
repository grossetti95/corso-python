# Genera un dizionario di prodotti
lista_spesa = []
subtotale = 0.0 # Inizializzo subtotale prima del ciclo


# Dichiaro gli input delle info prodotto
while True:
    prodotto = {}
    nome = str(input("Inserisci il nome: \n"))
    quantita = int(input("Quantità acquistata: \n"))
    prezzo = float(input("Prezzo unitario (prezzo con due decimali): \n"))
    
    # Inserisco gli input come chiavi nel dizionario del prodotto
    prodotto["Nome"] = nome
    prodotto["Quantità"] = quantita
    prodotto["Prezzo"] = prezzo
    
    # Dichiaro variabile totale per stampare totale prezzo prodotto
    totale = quantita * prezzo
    prodotto["Totale"] = totale

    # Subtotale
    subtotale += totale

    # Append nella lista della spesa
    lista_spesa.append(prodotto)
    
    # Ciclo indentato con condizione per uscire dal ciclo o renserimento altri prodotti
    while True:
        nuovo_prodotto = input("Vuoi inserire altro? s/n \n").lower()
        if nuovo_prodotto == "s" or nuovo_prodotto == "n":
            break
        else:
            print("Inserisci un carattere valido (s/n)")


    if nuovo_prodotto == "n":
        break

# Print finale di tutto il report
print("=== LISTA DELLA SPESA ===")
print(lista_spesa)
print(f"Il totale della spesa è {subtotale:.2f}")