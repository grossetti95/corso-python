def manipola_lista():
    
    # Lista di 15 numeri da manipolare
    numeri = list(range(1, 16))
    print(f"Lista originale: {numeri}\n")
    
    # 1: Estrazione con slicing
    # a) Primi 5 elementi
    primi_5 = numeri[:5]
    # b) Ultimi 5 elementi
    ultimi_5 = numeri[-5:]
    # c) Elementi dal 6° al 10°
    centrali = numeri[5:10]
    # d) Elementi in posizione dispari
    dispari = numeri[::2]
    # e) Elementi in posizione pari
    pari = numeri[1::2]
    # f) Lista al contrario
    al_contrario = numeri[::-1]
    
    print(f"Primi 5 elementi: {primi_5}")
    print(f"Ultimi 5 elementi: {ultimi_5}")
    print(f"Elementi dal 6° al 10°: {centrali}")
    print(f"Elementi in posizione dispari: {dispari}")
    print(f"Elementi in posizione pari: {pari}")
    print(f"Lista al contrario: {al_contrario}\n")
    
    #2: Modifica della lista
    # a) crea una copia della lista originale
    copia = numeri[:]
    # b) modifica il primo elemento con 99
    copia[0] = 99
    # c) modifica l'ultimo elemento con 0
    copia[-1] = 0
    # d) inserisci il valore 50 a metà della lista (indice 7)
    copia.insert(7, 50)
    # e) rimuove il valore 8 della lista
    copia.remove(8)
    # f) ordina la copia
    copia.sort()
    
    print(f"\nCopia modificata e ordinata: {copia}")
    print(f"Originale intatta:           {numeri}")
    
    # 3: enumerate per stampare ognu elemento
    # con il suo indice E se pari o dispari
    # formato: "Indice 0: 1 → dispari"
    print("\nLista con indice:")
    for i, n in enumerate(numeri):
        tipo = "pari" if n % 2 == 0 else "dispari"
        print(f"Indice {i:2}: {n:2} → {tipo}")
        
    # 4: costruisci queste liste con list comprehension
    # a) Lista dei quadrati dei numeri da 1 a 15
    quadrati = [n**2 for n in numeri]
    # b) Solo i quadrati superiori a 100
    quadrati_sopra_100 = [n for n in quadrati if n > 100]
    # c) stringhe nel formato "n²=quad" per ogni n in range(1,6)
    stringhe = [f"{n}²={n**2}" for n in range(1, 6)]
    
    print(f"\nQuadrati dei numeri da 1 a 15: {quadrati}")
    print(f"Quadrati superiori a 100: {quadrati_sopra_100}")
    print(f"Stringhe nel formato richiesto: {stringhe}")

if __name__ == "__main__":
    manipola_lista()