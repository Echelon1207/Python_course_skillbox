
numbers = [num for num in range(2,1001) if not [i for i in range(2,num) if not num % i]]
print(numbers)

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

numbers_2 = filter(is_prime, range(1,1001))
print(list(numbers_2))

#Более читабельное второе решение