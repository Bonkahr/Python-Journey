import mind_game
from user_info import user_info

info = user_info()
game = mind_game.MindGame(info[0], info[1], info[2])
game.game()
