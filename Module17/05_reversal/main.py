word = input('Введите слово: ')
fst_ind = word.index('h')
lst_ind = len(word)-1 - word[::-1].index('h')
print(word[lst_ind-1:fst_ind:-1])

