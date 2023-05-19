import random

fst_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
sec_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
win = []
for i in range(20):
    if fst_team[i] > sec_team[i]:
        win.append(fst_team[i])
    else:
       win.append(sec_team[i])
print('Победители тура: ', win)
