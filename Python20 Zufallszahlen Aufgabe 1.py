from random import randint


def teste(würfel_seiten: int, anzahl_würfe: int):
    anzahl_eins = 0
    for i in range(0, anzahl_würfe):
        zahl = randint(1, würfel_seiten)
        if zahl == 1:
            anzahl_eins += 1
    
    print(anzahl_eins)

teste(4, 200)