# Questo è un commento su una riga intera e python lo ignora

nome = "Peppe"
eta = 31
altezza = 1.65
developer = False

print("nome:", nome, "Età:", eta, "Altezza:", altezza, "Developer:", developer)

# Provo operazioni matematiche e vedo se le printa in terminal

a = 10
b = 5

print(f"{a} diviso {b} fa {a / b: .2f}")

# provo input

nome = input("Come ti chiami? ")
print(f"Ciao {nome}!")

#Provo un if

eta = input("Quanti anni hai? ")
if int(eta) >= 18:
    print("Sei Maggiorenne, bene!")
else:    print(f"Sei minorenne, mi dispiace! Torna tra {18 - int(eta)} anni")