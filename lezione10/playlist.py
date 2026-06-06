playlist = [
    {"titolo": "Bohemian Rhapsody", "artista": "Queen",        "durata": 354, "genere": "Rock",      "anno": 1975},
    {"titolo": "Blinding Lights",   "artista": "The Weeknd",   "durata": 200, "genere": "Pop",       "anno": 2019},
    {"titolo": "Lose Yourself",     "artista": "Eminem",       "durata": 326, "genere": "Hip-Hop",   "anno": 2002},
    {"titolo": "Shape of You",      "artista": "Ed Sheeran",   "durata": 234, "genere": "Pop",       "anno": 2017},
    {"titolo": "Hotel California",  "artista": "Eagles",       "durata": 391, "genere": "Rock",      "anno": 1977},
    {"titolo": "Smells Like Teen",  "artista": "Nirvana",      "durata": 301, "genere": "Rock",      "anno": 1991},
    {"titolo": "Sicko Mode",        "artista": "Travis Scott",  "durata": 312, "genere": "Hip-Hop",   "anno": 2018},
    {"titolo": "Bad Guy",           "artista": "Billie Eilish", "durata": 194, "genere": "Pop",       "anno": 2019},
    {"titolo": "Watermelon Sugar",  "artista": "Harry Styles",  "durata": 174, "genere": "Pop",       "anno": 2019},
    {"titolo": "God's Plan",        "artista": "Drake",         "durata": 198, "genere": "Hip-Hop",   "anno": 2018},
]

# Durata totale playlist in formato Xh Ym Zs
def durata_totale(playlist):
    totale_secondi = sum(canzone["durata"] for canzone in playlist)
    ore = totale_secondi // 3600
    minuti = (totale_secondi % 3600) // 60
    secondi = totale_secondi % 60
    return f"{ore}h {minuti}m {secondi}s"
