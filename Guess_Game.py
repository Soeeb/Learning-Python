import random
class Guess_game:
    def __init__(self, player_name):
        self.comp_num = random.randint(1, 10)
        self.guesses_so_far = 0
        self.game_over = False
        self.player_name = player_name

    def increment_goes(self):
        pass
        
    def check_game_over(self, the_input):
        #Check whether game has finished
        pass

player = input("What's your name?")
this_game = Guess_game(player)

while not this_game.game_over:
    '''Main loop for the game'''
    #get guess for this turn
    #increment number of goes
    #check whether too high or too low, display relevant message
    #check whether game over - either they got it right, or they've had 3 incorrect guesses. Call check_game_over()

#display correct message depending on whether they won or lost

