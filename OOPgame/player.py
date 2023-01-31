class Player(object):

    @property
    def lives(self):
        return self._lives

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print('Live can\'t be negative')
            self._lives = 0

    user_lives = property(_get_lives, _set_lives)

    def _set_level(self, level):
        bonus = 1000
        if level > 0:
            new_score = (level - self._level) * bonus
            if new_score > 0:
                self._score += new_score
            else:
                self._score = level * 1000
            self._level = level

        else:
            self._level = 1
            self._score = 0

    def _get_level(self):
        return self._level

    user_level = property(_get_level, _set_level)

    # decorators
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return f'Name: {self.name}, Lives: {self._lives}, Level: ' \
               f'{self._level}, Score: {self._score}'
