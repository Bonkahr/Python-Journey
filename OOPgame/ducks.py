class Wing(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print('weeeee, this is fun')
        elif self.ratio == 1:
            print("THis is hard work, but I'm frying")
        else:
            print("I think i'll jus walk")


class Duck(object):
    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print('Waddle, waddle, waddle')

    def swim(self):
        print('Come on it, the water\'s lovely')

    def quack(self):
        print('Quack quack')


class Penguin:
    def walk(self):
        print('Waddle, waddle, i waddle too')

    def swim(self):
        print('Come on it, but it\'s a bit chilly far south')

    def quack(self):
        print('Are you \'avin\' a larf? I\'m Penguin')


if __name__ == '__main__':
    donald = Duck()

    percy = Penguin()
