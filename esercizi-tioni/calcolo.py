# somma tutti i numeri dispari da 1 a 100
def somma_dispari(n):
    somma = 0
    for i in range(1, n + 1, 2):
        somma += i
    return somma

# calcola la somma dei numeri dispari da 1 a 100
risultato = somma_dispari(100)
print(risultato)