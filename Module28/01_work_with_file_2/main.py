class File:
    def __init__(self,file_name,mode='r'):
        self.file_name = file_name
        self.file = None
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(self.file_name,self.mode,encoding='utf-8')
            print('Файл с таким названием существует.')
            return self.file
        except:
            self.file = open(self.file_name,'w+', encoding='utf-8')
            print('Файла с таким названием нет.Создаем.')
            return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File('text.txt') as f:
    f.write('Hello!')
