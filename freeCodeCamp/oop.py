# class PartyAnimal:
#     x = 0
#
#     def party(self):
#         self.x = self.x + 2
#         print(self.x)

#
# an = PartyAnimal()
# an.party()
# an.party()
#
# k = 10.89
# print(dir(k))
# # print(k.denominator)
# print(k.real)


class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

# q.party()
# m.party()
# q.party()
