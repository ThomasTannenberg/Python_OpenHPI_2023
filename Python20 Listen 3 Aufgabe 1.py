from funktionen import buchstabenanzahl_ist_gerade

satz = "Du Suchender hast Mut und wirst die linke Allee nicht einschlagen sondern den Schatz entdecken sonst haben wir ihn gefunden"
liste = satz.split()
for wort in liste:
    if wort[1] == "e" or buchstabenanzahl_ist_gerade(wort):
        print(wort)
