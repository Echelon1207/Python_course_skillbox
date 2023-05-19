num = int(input('Сколько будет чисел? '))
numbers = []
for _ in range(num):
    digit = int(input('Введите число: '))
    numbers.append(digit)
print(sorted(numbers))