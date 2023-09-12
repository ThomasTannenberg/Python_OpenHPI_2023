from random import randint

woerterbuch = {
    'I': 'ich', 
    'You': 'du', 
    'We': 'wir', 
    'Love': 'liebe', 
    'Eat': 'essen', 
    'Cake': 'kuchen', 
    'Apple': 'apfel'
}

woerterbuch_eng_lst = []

for key in woerterbuch:
    woerterbuch_eng_lst.append(key)

while True:
    eng_word = woerterbuch_eng_lst[randint(0, len(woerterbuch_eng_lst)-1)]
    user_input = input(f'Was heißt {eng_word}? ')

    if user_input.lower() == 'ende':
        print('Auf Wiedersehen.')
        break
    elif user_input.lower() == woerterbuch.get(eng_word):
        print('Das ist richtig.')
    else:
        print('Das ist falsch.')

    