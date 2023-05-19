import os
path = input()
cnt_dirs = 0
cnt_files = 0
size = 0
for p,dirs,files in os.walk(path):
    cnt_dirs += len(dirs)
    cnt_files += len(files)
    for i in files:
        fp = os.path.join(p,i)
        size += os.path.getsize(fp)


print('Кол-во папок', cnt_dirs)
print('Кол-во файлов', cnt_files)
print('Размер', size)

