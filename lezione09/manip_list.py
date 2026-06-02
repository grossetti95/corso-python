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
    
    
if __name__ == "__main__":
    manipola_lista()    