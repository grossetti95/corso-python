# calcolatore voto scuola

voto = int(input("Inserisci il voto: "))
if voto >= 90:
    giudizio = "Ottimo"
elif voto >= 80:
    giudizio = "Distinto"
elif voto >= 70:
    giudizio = "Buono"
elif voto >= 60:
    giudizio = "Sufficiente"
else:
    giudizio = "Insufficiente"

print(f"Voto: {voto}/100 - {giudizio}")