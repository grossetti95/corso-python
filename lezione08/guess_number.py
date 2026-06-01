# Indovina il numero (fisso, in una variabile)

numero_da_indovinare = 42
max_tentativi = 3
tentativo = int(input("Indovina il numero: "))
while tentativo != numero_da_indovinare and max_tentativi > 1:
    max_tentativi -= 1
    print(f"Ti rimangono {max_tentativi} tentativi.")
    tentativo = int(input("Indovina il numero: "))
if tentativo == numero_da_indovinare:
    print("Hai indovinato!")
elif max_tentativi == 1:
    print("Hai esaurito i tentativi. Il numero era", numero_da_indovinare)