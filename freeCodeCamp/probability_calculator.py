import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, item in kwargs.items():
            for i in range(item):
                self.contents.append(key)

    def draw(self, balls):
        if balls >= len(self.contents):
            return self.contents
        else:
            new_contents = []
            for i in range(balls):
                ball_to_remove = self.contents[random.randint(0, len(self.contents) - 1)]
                self.contents.remove(ball_to_remove)
                new_contents.append(ball_to_remove)
            return new_contents

    def __str__(self):
        return f'Hat -> {self.contents}'


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int):
    balls = copy.copy(hat.contents)
    target_achieved = 0
    for i in range(num_experiments):
        d_balls = hat.draw(num_balls_drawn)
        checker = []
        for ball, number in expected_balls.items():
            if d_balls.count(ball) >= number:
                checker.append(True)
            else:
                checker.append(False)
        if False in checker:
            pass
        else:
            target_achieved += 1
        hat.contents = balls
    print(f'{target_achieved} / {num_experiments}')
    return target_achieved / num_experiments


hat1 = Hat(yellow=5, red=1, green=3, blue=9)
print(
    experiment(hat=hat1, expected_balls={'yellow': 2, 'blue': 1}, num_balls_drawn=7, num_experiments=100))
