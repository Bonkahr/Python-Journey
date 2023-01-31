class Animal:

    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name
        return self.name

    def set_her(self, name):
        self.name = name
        return self.name

    def __str__(self):
        return f'Name: {self.name}'


class Cat(Animal):

    def __init__(self, bobby):
        super().__init__(bobby)
        self.name = bobby

    def set_her(self, name):
        self.name = name
        return self.name


cat = Animal('Cat')
cat.set_name('Dog')
cat.set_her('Doggi')
print(cat)

cat = Cat('cattie')
cat.set_her('pato')
print(cat)