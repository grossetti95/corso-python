#SCONTRINO FISCALE

print ("=== Scontrino fiscale ===\n")

#input e conversione dei tipi
prodotto = input("Che prodotto hai acquistato? ")
prezzo = float(input("Quanto costa? (in euro) "))
quantita = int(input("Quante unità hai acquistato? "))

#dati cliente

nome_cliente = input("\nCome ti chiami? ")
eta_cliente = int(input("Quanti anni hai? "))
sesso_cliente = input("Qual è il tuo sesso? (M/F) ")
indirizzo_cliente = input("Qual è il tuo indirizzo? ")
piva_cliente = input("Hai una partita IVA? (S/N) ")
if piva_cliente.upper() == "S":
    piva_cliente = input("Inserisci la tua partita IVA: ")
else:    piva_cliente = None


#calcolo totale

totale = {int(prezzo) * 1.22 * int(quantita)}

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
else:    print(f"Partita IVA: {p.iva_cliente}")

