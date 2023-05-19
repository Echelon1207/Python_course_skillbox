def calculating_math_func(data):
    my_dict = dict()
    if data in my_dict:
        result = my_dict[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        my_dict[data] = result
    result /= data ** 3
    result = result ** 10
    return result

num = int(input('Введите число: '))
print(calculating_math_func(num))
