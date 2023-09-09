from daten import hauptspeise, nachtisch
if hauptspeise == "Suppe" and nachtisch == "Schokoladenpudding":
    print("Simon")
elif hauptspeise != "Kartoffeln" and nachtisch == "Obstsalat":
    print("Leonie")
elif (hauptspeise == "Kartoffeln" or hauptspeise == "Nudeln") and nachtisch == "Erdbeerjoghurt":
    print("Paul")
else:
    print("Mia")