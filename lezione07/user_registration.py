# Registrazione utente

# Username
while True:
    username = input("Inserisci il tuo username: ")
    
    if not username or len(username) < 5 or len(username) > 12:
        print("Username non può essere vuoto e deve essere compreso tra i 5 e i 12 caratteri. Riprova.")
    else:
        break
print(f"Benvenuto, {username}!")

#Password
caretteri_speciali = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" # Aggiunta di caratteri speciali per la validazione della password
while True:
    password = input("Inserisci la tua password: ")
    if not password or len(password) < 8 or len(password) > 20 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or password.isspace() or not any(char.isalnum() for char in password) or not any(char in caretteri_speciali for char in password):
        print("Password deve essere compresa tra gli 8 e i 20 caratteri e deve contenere almeno una lettera e un numero, un carattere speciale e non deve contenere spazi. Riprova.")
    else:
        break
print("Password accettata.")