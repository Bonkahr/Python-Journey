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

    def fly(self):
        self._wing.fly()


class Penguin:

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print('Waddle, waddle, i waddle too')

    def swim(self):
        print('Come on it, but it\'s a bit chilly far south')

    def quack(self):
        print('Are you avian a lard? I\'m Penguin')

    def aviate(self):
        print('I won the lottery and bought a learjet')


class Mallard(Duck):
    pass


class Flock:

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)
        # if isinstance(duck, Duck):
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("can't add duck, are you sure its not a " + str(
                type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError('Testing exception handler in migrate')
                # TODO remove this before release
            except AttributeError as e:
                print('One duck down')
                problem = e
        if problem:
            raise problem


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
