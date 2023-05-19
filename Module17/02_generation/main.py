n = int(input('Введите число: '))
numbers = [1 if n % 2 == 0 else n % 5 for n in range(n)]
print(numbers)
