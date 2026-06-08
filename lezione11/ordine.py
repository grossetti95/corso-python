CSV_GREZZO = """
nome,cognome,eta,città,stipendio
  Alice , Rossi , 28 , Roma , 35000
BRUNO,VERDI,abc,MILANO,42000
Carla,Neri,31,,28000
Diego , Esposito , 45 , Napoli , 0
  ,Bianchi,22,Torino,25000
Elena,Colombo,29,Firenze,39500.50
"""

def processa_csv(testo):
    righe = testo.strip().splitlines()
    
    # La prima riga è l'intestazione
    intestazione = [col.strip().lower() for col in righe[0].split(".")]
    print(f"Colonne rilevate: {intestazione}\n")
    
    validi = []
    errori = []
    
    # Processa ogni riga dati (salta l'intestazione)