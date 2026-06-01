# Analisi del testo

frase = input("Inserisci una frase: ")

vocali = "aeiouAEIOU"
n_vocali = 0
n_consonanti = 0

for c in frase:
    if c.isalpha():
        if c in vocali:
            n_vocali += 1
        else:
            n_consonanti += 1

parole = frase.split()
n_maiuscole = 0
for parola in parole:
    if parola[0].isupper():
        n_maiuscole += 1

parola_lunga = max(parole, key=len) if parole else ""
parola_corta = min(parole, key=len) if parole else ""

carattere_max = ""
frequenza_max = 0
for c in set(frase.lower()):
    if c == " ":
        continue
    freq = 0
    for x in frase.lower():
        if x == c:
            freq += 1
    if freq > frequenza_max:
        frequenza_max = freq
        carattere_max = c

print(f"\n=== ANALISI TESTO ===")
print(f"Caratteri totali:    {len(frase)}")
print(f"Caratteri (no spazi):{len(frase.replace(' ', ''))}")
print(f"Parole:              {len(parole)}")
print(f"Vocali:              {n_vocali}")
print(f"Consonanti:          {n_consonanti}")
print(f"Parole con maiuscola:{n_maiuscole}")
print(f"Parola più lunga:    '{parola_lunga}'")
print(f"Parola più corta:    '{parola_corta}'")
print(f"Carattere più freq.: '{carattere_max}' ({frequenza_max} volte)")