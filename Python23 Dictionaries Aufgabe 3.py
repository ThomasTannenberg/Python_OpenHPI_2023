from daten import anzahl_hinfahrt, anzahl_rueckfahrt

def berechne_anzahl(hin: int, rueck: int):
    return (hin + rueck)

berechne_anzahl(anzahl_hinfahrt, anzahl_rueckfahrt)