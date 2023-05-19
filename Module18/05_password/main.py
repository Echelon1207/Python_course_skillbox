password = input('Придумайте пароль: ')
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '1234567890'
count_word = 0
count_digit = 0

while True:
    for i in password:
        for j in alfabet:
            if i == j:
                count_word += 1
    for i in password:
        for j in digits:
            if i == j:
                count_digit += 1
    if len(password) >= 8 and count_word >= 1 and count_digit >= 3:
        print('Пароль надёжный')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    password = input('Придумайте пароль: ')