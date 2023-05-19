import zipfile

my_dict = dict()
with zipfile.ZipFile("voyna-i-mir.zip") as archive:
    for filename in archive.filelist:
        with archive.open(filename) as file:
            for sym in file.read().decode():
                if sym not in my_dict:
                    my_dict[sym] = 0
                my_dict[sym] += 1
sort_val = sorted(my_dict.values())
sort_dict ={}
for i in sort_val:
    for j in my_dict.keys():
        if my_dict[j] == i:
            sort_dict[j] = my_dict[j]

for key, val in sort_dict.items():
    print(key, val)

