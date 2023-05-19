with open('zen.txt') as file:
    word = file.read().split()
    file.seek(0)
    lines =  file.readlines()
    file.seek(0)
    letters = [i for i in file.read().lower() if i in 'abcdefghijklmnopqrstuvwxyz']

    print('Кол-во строк: ', len(lines))
    print('Кол-во слов: ', len(word))
    print('Кол-во букв: ', len(letters))
    print("Редкая буква", min(letters, key=letters.count))