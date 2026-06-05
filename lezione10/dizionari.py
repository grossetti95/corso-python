# Sintassi base dizionari
studente = {
    "nome": "Nfr",
    "cognome": "Ricchione",
    "eta": 28,
    "corsi": ["Cazzo in culo", "Bocchinologia", "Storia del cazzo"],
    "voto": 30,
    "frociamma": True
}

# Accesso ai valori del dizionario con parentesi quadre
print(studente["nome"])
print(studente["voto"])

# Accesso con .get() - restituisce None (o un default) se la chiave non esiste
print(studente.get("indirizzo"))  # Restituisce None
print(studente.get("nome"))  # Restituisce "Nfr"
print(studente.get("indirizzo", "Indirizzo non disponibile"))  # Restituisce il messaggio di default

# Modifica dei valori del dizionario
studente["voto"] = 30
print(studente["voto"])

# Aggiunge una nuova coppia chiave-valore
studente["universita"] = "La Sapienza Roma"
print(studente)

# Eliminare una coppia
del studente["eta"]
print(studente)

# Eliminare e ottenere il valore rimosso
voto_rimosso = studente.pop("voto")
print(voto_rimosso)
print(studente)

# Aggiornare più chiavi contemporaneamente con update()
studente.update({"eta": 23, "citta": "Roma", "voto": 29})
print(studente)