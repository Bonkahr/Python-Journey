import player
from enemy import Enemy, Troll, Vampire, VampireKing

# # james = player.Player('James')
# # print(james)
#
# # donkey = Troll('Donkey')
# # print(f'Donkey troll - {donkey}')
# #
# # dog = Troll('Dog')
# # print(f'dog troll - {dog}')
# #
# brother = Troll('Brother')
# print(brother)
# brother.take_damage(1)
# print(brother)
# #
# # donkey.grant()
# # dog.grant()
# # brother.grant()
#
# vampire = Vampire('Elijah')
# print(vampire)
# vampire.take_damage(3)
# print(vampire)
#
# while vampire.alive:
#     if not vampire.dodges():
#         vampire.take_damage(1)
#     print(vampire)

king = VampireKing('Micheal')
print(king)
king.take_damage(10)
print(king)



