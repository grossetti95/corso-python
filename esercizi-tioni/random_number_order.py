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

numeri_ordinati = []

for i in range(len(numeri)):
    valore_minimo = min(numeri)
    numeri_ordinati.append(valore_minimo)
    numeri.pop(numeri.index(valore_minimo))

print("Numeri ordinati:", *numeri_ordinati)