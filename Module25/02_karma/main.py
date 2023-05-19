import random


class Karma:

    karma_logs = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']
    def __init__(self,karma_count=0):
        self.karma_count = karma_count

    def one_day(self):

        while self.karma_count < 500:
            growth_karma = random.randint(1,7)
            num = random.randint(1,10)

            if num == 10:
                with open('karma.log', 'a') as file:
                    file.write(f'{random.choice(Karma.karma_logs)} \n')
                print('Исключение: ', random.choice(Karma.karma_logs))

            else:
                self.karma_count += growth_karma
                print(f'Карма увеличилась на {growth_karma} и равна {self.karma_count}')
        if self.karma_count >= 500:
            print('Карма достигла просветления!')

karma = Karma()
karma.one_day()