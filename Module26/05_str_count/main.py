import os

def gen_count(path):
    for roots, dirs, files in os.walk(path):
        for file in files:
            count = 0
            if os.path.join(roots,file).endswith('.py'):
                python_file = open(os.path.join(roots,file))
                for i in python_file.readlines():
                    if not (i == '\n' or  i.strip().startswith(("'''","#","'"))):
                        count +=1
                yield os.path.join(path,file), count
path = input('Введите путь: ')
for element in gen_count(path):
    print('Файл "{}": строк кода - {}'.format(element[0], element[1]))





