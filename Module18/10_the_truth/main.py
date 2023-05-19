alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def deshifr(message, key):
    step_1 = ''
    step_2 = ''
    for i in message:
        if i in alfabet:
            num = alfabet.find(i)
            step_1 += alfabet[num-key]
        else:
            step_1 += i
    replace_index = 3
    for word in step_1.split(' '):
        new_word = ''
        for index in range(len(word)):
            new_word += (word[index - replace_index % len(word)])
        if new_word.endswith('/'):
            replace_index += 1
        step_2 += new_word + ' '
        step_2 = step_2.replace('/', '\n')
    return step_2


text = input('Введите текст')

print(deshifr(text, 1))

