import random

class PlayCard:
    def __init__(self,cost_card,name_card):
        self.cost_card = cost_card
        self.name_card = name_card

class Player:
    def __init__(self,name,points=0):
        self.name= name
        self.points = points

class Game:
    sum_points = 0

    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
    def game_process(self,card1,card2):
        if self.sum_points >= 21:
            play_card_11.cost_card =1
            self.player1.points += card1.cost_card
            self.player2.points += card2.cost_card
            print(self.player1.points, card1.name_card)
        else:
            self.player1.points += card1.cost_card
            self.player2.points += card2.cost_card
            self.sum_points = (self.player1.points + self.player2.points)
            print(self.player1.points,card1.name_card)

    def winner(self):
        if self.player1.points == 21 and self.player2.points == 21:
            print('Ничья')
        elif self.player1.points > 21 and self.player2.points <= 21:
            print(f'Победил {self.player2.name}')
        elif self.player2.points > 21 and self.player1.points <= 21:
            print(f'Победил {self.player1.name}')
        else:
            print('Победителей нет')

play_card_2 = PlayCard(2, 'двойка')
play_card_3 = PlayCard(3, 'тройка')
play_card_4 = PlayCard(4, 'четверка')
play_card_5 = PlayCard(5, 'пятерка')
play_card_6 = PlayCard(6, 'шестерка')
play_card_7 = PlayCard(7, 'семерка')
play_card_8 = PlayCard(8, 'восьмерка')
play_card_9 = PlayCard(9, 'девятка')
play_card_10 = PlayCard(10, 'десятка')
play_card_11 = PlayCard(11, 'туз')
play_card_12 = PlayCard(10, 'валет')
play_card_13 = PlayCard(10, 'дама')
play_card_14 = PlayCard(10, 'король')

deck = [play_card_2, play_card_3, play_card_4, play_card_5, play_card_6, play_card_7, play_card_8, play_card_9, play_card_10, play_card_11, play_card_12, play_card_13, play_card_14 ]
player = Player('игрок')
comp = Player('компьютер')
game = Game(player, comp)

while True:
    r1= random.randint(0,12)
    r2 = random.randint(0,12)
    request = input('Введите "взять" чтобы продолжить или "стоп" чтобы остановиться: ')
    if request == 'взять':
        game.game_process(deck[r1],deck[r2])
    elif request == 'стоп':
        break

game.winner()