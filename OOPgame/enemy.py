import math
import random


class Enemy:
    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f'I took {damage} points and have {self.hit_points} left.')
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f'{self.name} lost a life')

            else:
                print(f'{self.name} is dead')
                self.alive = False

    def __str__(self):
        return f'Name: {self.name}, Lives: {self.lives}, ' \
               f'Hit Points: {self.hit_points}.'


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=4, lives=2)

    def grant(self):
        print(f'Me {self.name}. {self.name} stomp you')


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f'*****{self.name} doges *****')
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self.hit_points = 140
        self.lives = 6

    def take_damage(self, damage):
        super().take_damage(damage // 4)

