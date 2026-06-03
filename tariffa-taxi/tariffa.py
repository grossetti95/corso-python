print("servizio taxi Nfricchione srl")

tariffa_base = 3.00 # Tariffa base in euro
costo_km = 1.20 # Costo per chilometro in euro
giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
corse_fatte = int(input("quante corse hai fatto? "))
km_percorsi = float(input("quanti km hai percorso? "))
giorno_settimana = input("in che giorno della settimana hai fatto la corsa? ")
orario_corsa = int(input("a che ora hai fatto la corsa? (in formato 24h, es. 14.30) "))

# Calcolo del costo totale
if giorno_settimana in giorni_settimana and giorno_settimana in ["Sabato", "Domenica"]:
    costo_totale = tariffa_base + (costo_km * km_percorsi) + 1.5 # Tariffa maggiorata del 50% nei weekend
else:
    costo_totale = tariffa_base + (costo_km * km_percorsi) # Tariffa normale

# Sconto 10% per utente con più di 10 corse
if corse_fatte > 10:
    costo_totale *= 0.9
    
# Maggiorazione 2€ per corse dalle 22:00 alle 06:00
if orario_corsa >= 22 or orario_corsa <= 6:
    costo_totale += 2
    
# Ricevuta finale
print(f"Il costo totale della corsa è: {costo_totale:.2f} euro")
print(f"Grazie per aver scelto il servizio taxi Nfricchione srl!")