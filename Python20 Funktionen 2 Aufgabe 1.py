from daten import liste, buchstabe, anzahl

def stadt_mit(liste: list, buchstabe: str, zahl: int):
    ausgabe_liste = []
    for wort in liste:
        if wort[0] == buchstabe and len(wort) <= zahl:
            ausgabe_liste.append(wort)

    return ausgabe_liste

print(stadt_mit(liste, buchstabe, anzahl))