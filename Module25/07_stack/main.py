class Stek:
    def __init__(self, my_list=None):
        if my_list is None:
            my_list = []
        self.my_list = my_list
    def add(self,elem):
        self.my_list.append(elem)
        return self.my_list
    def delete(self):
        del_elem = self.my_list.pop(-1)
        return f'Удален элемент {del_elem}.\nТекущий список {self.my_list}'

class TaskManager:
   def __init__(self,my_dict=None):
        if my_dict is None:
            my_dict = {}
        self.my_dict = my_dict
   def new_task(self,task,priority):
       self.my_dict[task] = [priority]
       return self.my_dict
   def sort(self):
       sort_dict = dict(sorted(self.my_dict.items(), key=lambda f: f[1]))
       for k,v in sort_dict.items():
           print(*v,k)

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.sort()

