from daten import woerterbuch, satz

satz_als_liste = satz.split(' ')
#print(satz_als_liste)

for i in range (len(satz_als_liste)):
    print(woerterbuch[satz_als_liste[i]])