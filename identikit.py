# Nome e cognome

nome = input("Buongiorno. Cnome e cognome, prego. ")
print(f"Salve {nome}.")

#età

eta = input("Quanti anni ha? ")
if int(eta) >= 18:
    print("E' maggiorenne, possiamo continuare la conversazione!")
else:    print(f"Non è maggiorenne, mi dispiace! Torni tra {18 - int(eta)} anni")
if int(eta) < 18:
    exit()

# Calcolo BMI

altezza = input("Quanto è alto? (in metri) ")
peso = input("Quanto pesa? (in kg) ")
bmi = int(peso) / (float(altezza) ** 2)
print(f"Il tuo BMI è {bmi:.2f}, lei si trova in unoi stato di {'sottopeso' if bmi < 18.5 else 'normopeso' if bmi < 25 else 'sovrappeso' if bmi < 30 else 'obesità'}.")

# Chiedo il lavoro

lavoro = input("Che lavoro fa? ")
print(f"Interessante, lavorare come {lavoro} deve essere stimolante!")

# Riepilogo di tutto e print finale

print(f"Riepilogo: {nome} ha {eta} anni, è alto {altezza} metri, pesa {peso} kg, ha un BMI di {bmi:.2f} e lavora come {lavoro}.")
print("Grazie per aver condiviso queste informazioni con me e spero di rivederti presto!")