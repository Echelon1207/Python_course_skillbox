import os


def gen_files_path(find,path):
    for roots, dirs, files in os.walk(path):
        for dir in dirs:
            current_path = os.path.join(path, dir)
            find_dir = os.path.join(path,find)
            if os.path.isdir(current_path):
                print(current_path)
                if current_path == find_dir:
                    yield True
                yield False


find = input('Какой каталог ищем?')
path = input('Введите путь где искать папку: ')
result = gen_files_path(find, path)
for i in result:
    if i==True:
        print('Каталог найден!')
        break
