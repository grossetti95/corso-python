def statistiche(numeri):
    """Restituisce minimo, massimo e media di una lista di numeri."""
    return min(numeri), max(numeri), sum(numeri) / len(numeri)

# La funzione restituisce una tupla
risultato = statistiche([3, 7, 2, 9, 1])
print(risultato)  # Output: (1, 9, 4.4)

# Unpacka subito (più utile)
minimo, massimo, media = statistiche([3, 7, 2, 9, 1])
print(f"Minimo: {minimo}, Massimo: {massimo}, Media: {media}")