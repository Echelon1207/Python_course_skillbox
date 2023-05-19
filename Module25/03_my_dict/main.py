class MyDict:
    def __init__(self,my_dict):
        self.__my_dict = my_dict

    def get_my_dict(self,key):
        for i in self.__my_dict.keys():
            if key not in self.__my_dict:
                return 0
            else:
                return self.__my_dict

dict = {}
for i in range(3):
    word = input('Введите ключ и значение через пробел: ').split(' ')
    dict[word[0]] = word[1]

key = input('Какой ключ ищем в словаре?: ')
test = MyDict(dict)
print(test.get_my_dict(key))