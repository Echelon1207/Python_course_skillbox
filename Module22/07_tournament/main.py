with open('first_tour.txt') as one:
    team_list = one.readlines()
    team_dict = dict()
    win_team = dict()
    for i in team_list[1:]:
        team_dict[i.strip()[:-2]] = i.strip()[-2:]
    for key,val in team_dict.items():
        if int(val) > 80:
            win_team[key] = val

with open('second_tour.txt', 'w') as result:
    for key,val in win_team.items():
        result.write(f'{key} {val} \n')
