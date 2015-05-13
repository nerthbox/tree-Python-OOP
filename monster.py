import random

COLORS = ['yellow', 'blue', 'green', 'orange', 'brown', 'white', 'black', 'purple',
          'grey', 'red', 'magenta', 'dick', 'flesh', 'nigger']


class Monster:
    min_hitPoints = 1
    max_hitPoints = 1
    min_exp = 1
    max_exp = 1
    weapon = 'sword'
    sound = 'wolololololol'

    def __init__(self, **kwargs):
        self.hitPoints = random.randint(self.min_hitPoints, self.max_hitPoints)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)


    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hitPoints,
                                              self.exp)


    def battleCry(self):
        return self.sound.upper()

class Goblin(Monster):
    max_hitPoints = 3
    max_exp = 2
    sound = 'squerf'
    

class Troll(Monster):
    min_hitPoints = 3
    max_hitPoints = 5
    min_exp = 2
    max_exp = 6
    sound = 'growl'


class Dragon(Monster):
    min_hitPoints = 5
    max_hitPoints = 10
    min_exp = 6
    max_exp = 10
    sound = 'rawr'
