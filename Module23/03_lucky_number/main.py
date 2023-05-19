import random

text = ['Вас постигла неудача!', 'Прерывание программы!', "Конец!"]
count = 0

with open('out_file.txt', 'w') as file:
    try:
        while True:
            num = int(input("Введите число: "))
            count += num
            file.write(f'{str(num)} \n')
            if count == 777:
                print('Вы успешно выполнили условие для выхода из порочного цикла!')
                break
            elif 13 == random.randint(1,13):
                raise Exception
    except Exception:
        print(random.choice(text))