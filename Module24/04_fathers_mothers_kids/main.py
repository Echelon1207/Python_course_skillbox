class Parent:
    def __init__(self,name='мама',age=40,count_children=1):
        self.name = name
        self.age = age
        self.count_children = count_children

    def info(self):
        print('Я {}, мне {} лет, у меня {} ребенок'.format(self.name,self.age,self.count_children))

    def relax_children(self,Children):
         if Children.condition_relax == 0:
             print('Успокаиваем ребенка!')
             Children.condition_relax = 1
         else:
             print('Ребенок спокоен!')

    def eat_children(self,Children):
        if Children.hunger == 0:
            print('Кормим ребенка!')
            Children.hunger = 1
        else:
            print('Ребенок пока не голоден!')


class Children:
    condition_relax = {0:'плачет',1 : "спокоен"}
    hunger = {0 : 'голоден',1 : 'сыт'}
    def __init__(self, name='Tom', age=10, condition_relax=0, hunger=0):
        self.name = name
        self.age = age
        self.condition_relax = condition_relax
        self.hunger = hunger

    def info(self):
        print('Ребенок {} сейчас {} и {}'.format(self.name,Children.condition_relax[self.condition_relax],Children.hunger[self.hunger]))


mother = Parent()
ch1= Children()

mother.info()
ch1.info()
mother.eat_children(ch1)
mother.relax_children(ch1)
ch1.info()
print()

father = Parent('папа',45,1)
ch2 = Children('Ann',12)

father.info()
ch2.info()
father.eat_children(ch2)
father.relax_children(ch2)
ch2.info()


