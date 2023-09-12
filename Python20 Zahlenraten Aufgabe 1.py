from random import randint

rnd_nummer = randint(1, 100)


while True:
    player_number = int(input('Gib eine Zahl ein: '))

    try:
        if player_number == rnd_nummer:
            print('Herzlichen Glückwunsch')
            break
        elif player_number < rnd_nummer:
            print('Zu klein')
        else:
            print('Zu Groß')
            
    except ValueError:
        print(f'{player_number} ist keine gültige Zahl!') 
