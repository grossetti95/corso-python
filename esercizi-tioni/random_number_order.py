# Genera un array di 20 numeri casuali, poi stampa i numeri nell'ordine in cui vengono generati, e poi in ordine crescente.

import random

numeri = random.sample(range(1, 81), 20)  # genera 20 numeri unici tra 1 e 80

tentativi = 5

while tentativi > 0:
    try:
        guess = int(input("Inserisci un numero tra 1 e 80: "))
        if guess < 1 or guess > 80:
            print("Il numero deve essere tra 1 e 80.")
            continue
    except ValueError:
        print("Per favore, inserisci un numero valido.")
        continue

    if guess in numeri:
        print("Hai indovinato! Il numero è nella lista.")
        break
    else:
        tentativi -= 1
        print(f"Numero sbagliato. Ti rimangono {tentativi} tentativi.") #tioni tiandri (rea) sei un ricchione schifoso
    
if tentativi == 0:
    print("Hai esaurito i tentativi")

print("Numeri generati:", *numeri)
print("Numeri in ordine crescente:", *sorted(numeri))