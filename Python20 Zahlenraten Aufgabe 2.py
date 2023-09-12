from random import randint


min_val = 1
max_val = 100

while True:
    rnd_nummer = randint(min_val, max_val)
    print(min_val, max_val)
    user_input = input(f'{rnd_nummer}? ')

    if user_input == 'r':
        break
    elif user_input == 'k':
        min_val = rnd_nummer + 1
    elif user_input == 'g':
        max_val = rnd_nummer - 1

        

