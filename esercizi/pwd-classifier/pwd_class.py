# Classificatore punteggio per Password

from getpass import getpass

print("Benvenuto al classificatore di sicurezza per password!")
password = getpass("Inserisci la tua password: ")
punteggio = 0

# Verifica lunghezza password
if len(password) > 8:
    punteggio += 1
if len(password) < 12:
    punteggio += 1
    
# Verifico presenza di lettere maiuscole
if any(c.isupper() for c in password):
    punteggio += 1
    
# Verifico presenza di lettere minuscole
if any(c.islower() for c in password):
    punteggio += 1

# Verifico presenza di numeri
if any(c.isdigit() for c in password):
    punteggio += 1

# Verifico presenza di caratteri speciali
if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password):
    punteggio += 1

# Verifico che la password non contenga la parola Password (case insensitive)
if "password" not in password.lower():
    punteggio += 1
    
# Classifico la password in base al punteggio
if punteggio <= 2:
    print("La tua password è debole. Considera di migliorarla.")
elif punteggio <= 4:
    print("La tua password è media. Potrebbe essere più sicura.")
elif punteggio <= 6:
    print("La tua password è forte. Ottimo lavoro!")
else:
    print("La tua password è molto forte. Complimenti!")
    
# Mostra il punteggio totale
print(f"Il punteggio totale della tua password è: {punteggio}/7")

# Mostra i criteri soddisfatti e quelli non soddisfatti
print("Criteri soddisfatti:")
if len(password) > 8 and len(password) < 12:
    print("- Lunghezza adeguata (9-11 caratteri)")
if any(c.isupper() for c in password):
    print("- Contiene lettere maiuscole")
if any(c.islower() for c in password):      
    print("- Contiene lettere minuscole")
if any(c.isdigit() for c in password):
    print("- Contiene numeri")
if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password):
    print("- Contiene caratteri speciali")
if "password" not in password.lower():
    print("- Non contiene la parola 'password'")

# Mostra i criteri non soddisfatti
print("Criteri non soddisfatti:")
if not (len(password) > 8 and len(password) < 12):
    print("- Lunghezza non adeguata (deve essere tra 9 e 11 caratteri)")
if not any(c.isupper() for c in password):
    print("- Non contiene lettere maiuscole")
if not any(c.islower() for c in password):
    print("- Non contiene lettere minuscole")
if not any(c.isdigit() for c in password):
    print("- Non contiene numeri")
if not any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password):
    print("- Non contiene caratteri speciali")
if "password" in password.lower():
    print("- Contiene la parola 'password' (non sicuro)")
    
# Messaggio se tutti i criteri sono soddisfatti
if punteggio == 7:
    print("La tua password soddisfa tutti i criteri di sicurezza! Ottimo lavoro!")

# Saluta
print("Grazie per aver utilizzato il classificatore di sicurezza per password! Ricorda di scegliere sempre password forti e sicure.")