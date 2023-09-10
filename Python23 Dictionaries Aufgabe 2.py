from daten import woerterbuch

gespiegelt = {}
print(woerterbuch)

for word in woerterbuch:
    print(word)

for value in woerterbuch.values():
    print(value)

for paar in woerterbuch.items():
    gespiegelt[paar[1]] = paar[0]