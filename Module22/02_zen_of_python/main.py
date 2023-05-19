with open('zen.txt') as file:
    text = file.readlines()
    print(*text[::-1], sep ='')
