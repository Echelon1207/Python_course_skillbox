def move(n, x, y):
    if n == 1:
        print("Переложить диск 1 со стержня номер", x, "на стержень номер", y)
    else:
        move(n - 1, x, 6 - x - y)
        print("Переложить диск", n, "со стержня номер ", x, "на стержень номер", y)
        move(n - 1, 6 - x - y, y)


n = int(input('Введите количество дисков: '))
move(n, 1, 3)
