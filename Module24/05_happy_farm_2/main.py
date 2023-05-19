class Gardener:
    def __init__(self,name='садовник',garden_patotes = 'картошка'):
        self.name = name
        self.garden_patotes = garden_patotes

    def care(self,Patotes):
        if 0 <= Patotes.stages < 3:
            print('Поливаем и удобряем картошку! Теперь она вырастет быстрее')
            Patotes.stages += 1
    def collect(self,Patotes):
        print("Картошка уже созрела.Собрать? Y/N")
        answer = input().lower()
        if answer == 'y':
            Patotes.stages = 0
            print('Картошка собрана!')

class Patotes:
    stages = {0 : 'Отсутствует', 1 : 'Росток', 2 : 'Зеленая', 3 : 'Созрела'}
    def __init__(self,index=1):
        self.index = index
        self.stages = 0
    def grow(self):
        if self.stages < 3:
            self.stages += 1
        self.info()
    def info(self):
        print('Картошка на {} грядке сейчас в стадии {}'.format(self.index,Patotes.stages[self.stages]))

    def is_ripe(self):
        if self.stages == 3:
            return True
        return False


class GardenPatotes:
    def __init__(self,count):
        self.patotes = [Patotes(index) for index in range(1,count+1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i in self.patotes:
            i.grow()
    def all_ripe(self):
        for i in self.patotes:
            if not i.is_ripe():
                return False
            return True

    def count_patotes(self):
        count = 0
        for i in self.patotes:
            if i.is_ripe():
                count += 1
        return count


my_garden = GardenPatotes(5)
patotes = Patotes()
man = Gardener()

man.care(patotes)
patotes.info()
man.care(patotes)
man.care(patotes)
patotes.info()
man.collect(patotes)
patotes.info()