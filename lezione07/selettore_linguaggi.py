# Questo esercizio è una prova di array

linguaggi_programmazione = ["python", "java", "c++", "javascript", "ruby"]
print("Seleziona un linguaggio di programmazione:")
linguaggio = input("Quale linguaggio usi?").lower()  # Converti l'input in minuscolo per confronto case-insensitive

# Confronto scelta utente con array di linguaggi

if linguaggio in linguaggi_programmazione:
    print(f"Hai selezionato {linguaggio}. E' supportato, ottima scelta!")
else:
    print(f"Hai selezionato {linguaggio}. Mi dispiace, non è supportato.")