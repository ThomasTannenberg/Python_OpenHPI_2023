

try:
    first_num = int(input('Erste Zahl?'))
    operation = input('Rechenoperation?')
    second_num = int(input('Zweite Zahl?'))

    if operation == '+':
        print(first_num + second_num)
    elif operation == '-':
        print(first_num - second_num)
    elif operation == '*':
        print(first_num * second_num)
    elif operation == '/':
        print(first_num / second_num)
        
except ValueError:
    print('Fehler, der Text kann nicht in eine Zahl umgewandelt werden.')
