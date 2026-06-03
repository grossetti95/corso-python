# Sequenza di Fibonacci

n = int(input("Quanti termini di Fibonacci? "))

if n <= 0:
    print("Inserisci un numero positivo.")
else:
    a, b = 0, 1
    sequenza = []
    
    for _ in range(n):
        sequenza.append(a)
        a, b = b, a + b

    somma = 0
    n_pari = 0
    n_dispari = 0
    for num in sequenza:
        somma += num
        if num % 2 == 0:
            n_pari += 1
        else:
            n_dispari += 1
            
    print(f"\nSequenza: {', '.join(str(x) for x in sequenza)}")
    print(f"Ultimo termine:  {sequenza[-1]}")
    print(f"Somma:           {somma}")
    print(f"Pari:            {n_pari}")
    print(f"Dispari:         {n_dispari}")

    if n >= 2 and sequenza[-2] != 0:
        rapporto = sequenza[-1] / sequenza[-2]
        print(f"Rapporto φ:      {rapporto:.6f} (φ ≈ 1.618034)")