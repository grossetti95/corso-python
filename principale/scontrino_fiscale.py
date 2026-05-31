#SCONTRINO FISCALE

print ("=== Ricevuta fiscale ===\n")

#input e conversione dei tipi

prodotto = input("Che prodotto hai acquistato? ")
prezzo = float(input("Quanto costa? (in euro) "))
quantita = int(input("Quante unità hai acquistato? "))

#dati cliente

nome_cliente = input("\nCome ti chiami? ")
eta_cliente = int(input("Quanti anni hai? "))
sesso_cliente = input("Qual è il tuo sesso? (M/F/Altro) ")
indirizzo_cliente = input("Qual è il tuo indirizzo? ")
piva_cliente = input("Hai una partita IVA? (S/N) ")
if piva_cliente.upper() == "S":
    piva_cliente = input("Inserisci la tua partita IVA: ")
else:    piva_cliente = None

#calcolo totale

if piva_cliente is None:
    totale = float(prezzo) * int(quantita)
else:
    prezzo_scontato = float(prezzo) * 0.55
    iva = prezzo_scontato * 0.22
    totale = (prezzo_scontato + iva) * int(quantita)

    print(f"Prezzo scontato: {prezzo_scontato:.2f} €")
    print(f"IVA (22%):       {iva:.2f} €")
    print(f"Totale:          {totale:.2f} €")

print(f"Il totale è: {totale} €")

#output formattato con f-string

print("\n=== Dettaglio scontrino ===")
print(f"Prodotto: {prodotto}")
print(f"Prezzo: {prezzo} €")
print(f"Quantità: {quantita}")
print(f"Totale: {totale} €")
print("\n=== Dati cliente ===")
print(f"Nome: {nome_cliente}")
print(f"Età: {eta_cliente} anni")
print(f"Sesso: {sesso_cliente}")
print(f"Indirizzo: {indirizzo_cliente}")
if piva_cliente is None:
    print(f"Il cliente non ha una partita IVA.")
else:    print(f"Partita IVA: {piva_cliente}")

