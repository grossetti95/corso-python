# Dati in un array e input per indovinare

def indovina_il_frocio():
    # Array di froci
    froci = ["jenk", "chelaudio", "tisoni", "tipeppe", "phil", "mrmr"]
    # Input dell'utente case-insensitive
    indovina = input("Indovina il frocio: ")
    
    # Rendo input case-insensitive
    indovina = indovina.lower()
    
    # Limite a 3 tentativi
    tentativi = 2
    while tentativi > 0:
        if indovina in froci:
            print("Validi!")
            break
        else:
            tentativi-=1
            print(f"Non è un frocio valido. Ti rimangono {tentativi} tentativi.")
            indovina = input("Indovina il frocio: ")
    if tentativi == 0:
        print("Sei un ricchione di merda, hai perso!")
        
if __name__ == "__main__":
    indovina_il_frocio()