violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
count_songs = int(input('Сколько песен выбираем? '))
minutes = 0
for i in range(count_songs):
    song = input('Введите название песни: ').lower()
    for j in violator_songs:
        if j[0].lower() == song:
            minutes += j[1]
print(minutes)