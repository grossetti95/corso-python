# Genera un dizionario di prodotti
lista_spesa = []
prodotto = {}

# Dichiaro gli input delle info prodotto
while True:
    
    nome = input("Inserisci il nome: \n")
    quantita = int(input("Quantità acquistata: \n"))
    prezzo = float(input("Prezzo unitario (prezzo con due decimali): \n"))
    
    prodotto["Nome"] = nome
    prodotto["Quantità"] = quantita
    prodotto["Prezzo"] = prezzo
    

    # Dichiaro variabile totale per stampare totale prezzo prodotto
    totale = quantita * prezzo
    prodotto["Totale"] = totale
    
    nuovo_prodotto = input("Vuoi inserire altro? s/n \n")
    
    # Append nella lista della spesa
    lista_spesa.append(prodotto)
    
    # Subtotale
    subtotale = []
    subtotale.append(totale)
      
    # Condizione per uscire dal ciclo
    if nuovo_prodotto == "n":
        break
    
# Somma degli indici di subtotale
subtot = sum(subtotale)


print("Ecco la lista della spesa")
print(lista_spesa)
print(subtot)