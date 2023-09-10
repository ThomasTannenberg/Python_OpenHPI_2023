from random import randint

def teste(würfel_seiten: int, anzahl_würfe: int):
    anzahl = {'1': 0} 
    for i in range(anzahl_würfe):
        zahl = randint(1, würfel_seiten)
        if zahl == 1:
            anzahl['1'] += 1

    print(anzahl['1'])

teste(4, 200)