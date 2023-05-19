players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

a = []
for key,val in players.items():
         a.append((key[0],key[1],val[0],val[1],val[2]))
print(a)
