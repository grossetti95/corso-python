import sys

print("╔══════════════════════════════════════════╗")
print("║      SISTEMA PRENOTAZIONI HOTEL          ║")
print("╚══════════════════════════════════════════╝\n")

# Dati cliente
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisclearci il tuo cognome: ")
data_nascita = input("Inserisci la tua data di nascita (gg/mm/aaaa): ")
email = input("Inserisci la tua email: ")
cellulare = int(input("Inserisci il tuo numero di cellulare: "))
tipo_camera = (input("Inserisci il tipo di camera (singola/doppia/suite): ")).lower()

# Dati prenotazione
data_check_in = input("Inserisci la data di check-in (gg/mm/aaaa):")
data_check_out = input("Inserisci la data di check-out (gg/mm/aaaa):")
numero_ospiti = int(input("Inserisci il numero di ospiti: "))
colazione_inclusa = input("Colazione inclusa? (sì/no): ").lower()

# Calcolo del costo totale
costo_camera = 0
if tipo_camera == "singola":
    costo_camera = 80
elif tipo_camera == "doppia":
    costo_camera = 120
elif tipo_camera == "suite":
    costo_camera = 200

costo_colazione = 0
if colazione_inclusa == "sì":
    costo_colazione = 10 * numero_ospiti * (int(data_check_out.split('/')[0]) - int(data_check_in.split('/')[0]))
costo_totale = costo_camera * (int(data_check_out.split('/')[0]) - int(data_check_in.split('/')[0])) + costo_colazione

# Caparra 30%
caparra = costo_totale * 0.3

# Requisiti minimi stanze
if tipo_camera == "singola" and numero_ospiti > 1:
    print("Errore: la camera singola può ospitare solo 1 persona.")
elif tipo_camera == "doppia" and numero_ospiti > 2:
    print("Errore: la camera doppia può ospitare solo 2 persone.")
elif tipo_camera == "suite" and numero_ospiti > 4:
    print("Errore: la suite può ospitare fino a 4 persone.")

# Output
if int(data_check_out.split('/')[0]) - int(data_check_in.split('/')[0]) <= 0:
    print("Errore: la data di check-out deve essere successiva alla data di check-in.")
else:
    print(f"Il costo totale della prenotazione è: {costo_totale} euro.")
    print(f"La caparra da versare è: {caparra} euro.")