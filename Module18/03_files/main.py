file = input('Название файла: ').lower()
simbols = '@','№','$','%','^','&','*','(',')', ' \ '
if file.startswith(simbols):
    print('Ошибка: название начинается на один из специальных символов.')
elif not file.endswith('.txt') or file.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')
