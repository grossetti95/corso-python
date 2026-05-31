from getpass import getpass
import json
import os

# Nome del database
DATABASE_FILE = "utenti_db.json"

# Carico i dati dal json
def load_database(): 
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []  # Se il file è corrotto, restituisce una lista vuota
    return []  # IMPORTANTE: Se il file non esiste, restituisce una lista vuota invece di None

# Salvo i dati nel json
def save_database(database):
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(database, file, indent=4)

# Setto un database interno per memorizzare le informazioni degli utenti
database_utenti = load_database()

print("Benvenuto al processo di registrazione!")

# --- 1. VALIDAZIONE USERNAME ---
while True:
    username = input("Inserisci il tuo username: ")
    
    # Controlliamo se lo username esiste già nella lista di dizionari
    username_gia_presente = any(user['username'] == username for user in database_utenti)
    
    if username_gia_presente:
        print("Username già utilizzato. Scegline un altro.")
    elif not username or len(username) < 5 or len(username) > 12:
        print("Username non può essere vuoto e deve essere compreso tra i 5 e i 12 caratteri. Riprova.")
    else:
        break
print(f"Username accettato: {username}!")

# --- 2. VALIDAZIONE PASSWORD ---
caratteri_speciali = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" 

while True:
    password = getpass("Inserisci la tua password: ")
    
    # Controlliamo prima se NON rispetta i requisiti
    if (not password or 
        len(password) < 8 or 
        len(password) > 20 or 
        not any(char.isdigit() for char in password) or 
        not any(char.isalpha() for char in password) or
        not any(char.isupper() for char in password) or
        " " in password or 
        not any(char in caratteri_speciali for char in password)):
        print("La password non rispetta i requisiti di sicurezza. Servono almeno una lettera maiuscola, un numero e un carattere speciale, inoltre deve essere compresa tra gli 8 e i 20 caratteri. Riprova.")
        continue  # Ricomincia il ciclo dall'inizio, ignorando la conferma sotto
    
    # Se il programma arriva qui, significa che la password è sicura
    conferma_password = getpass("Conferma la tua password: ")
    if password != conferma_password:
        print("Le password non corrispondono. Riprova da capo.")
        # Non serve mettere nulla, il ciclo ricomincerà da solo dall'inizio
    else:
        # Se sono uguali, la registrazione della password è finita!
        break
print("Password accettata.")

# --- 3. VALIDAZIONE EMAIL ---
while True:
    email = input("Inserisci il tuo indirizzo email: ")
    
    # Controlliamo se l'email esiste già nella lista di dizionari
    email_gia_presente = any(user['email'] == email for user in database_utenti)
    
    if email_gia_presente:
        print("Indirizzo email già utilizzato. Scegline un altro.")
    elif not email or "@" not in email or "." not in email:
        print("Indirizzo email non valido. Riprova.")
    else:
        break
print(f"Indirizzo email accettato: {email}.")

# --- 4. SALVATAGGIO DEI DATI ---
# Aggiungiamo il nuovo utente come dizionario all'interno della lista globale
database_utenti.append({
    "username": username, 
    "email": email, 
    "password": password
})
save_database(database_utenti)

# --- 5. RIEPILOGO FINALE ---
print("\n--- RIEPILOGO REGISTRAZIONE ---")
print("Utenti registrati:")
for user in database_utenti:
    print(f"- {user['username']}")

print("\nIndirizzi email registrati:")
for user in database_utenti:
    print(f"- {user['email']}")
print("\nRegistrazione completata con successo, grazie per aver scelto il nostro servizio. Nfr è un ricchione")