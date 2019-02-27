import random
class Guess_game:
    def __init__(self, player_name):
        self.comp_num = random.randint(1, 10)
        self.guesses_so_far = 0
        self.game_over = False
        self.player_name = player_name

    def increment_goes(self):
        self.guesses_so_far += 1
        
    def check_game_over(self, the_input):
        #Check whether game has finished
        self.the_input = the_input
        if self.guesses_so_far == 3:
             self.game_over = True
            print(f"{self.player_name} You Lose!")

        elif self.the_input == self.comp_num:
            self.game_over = True
            print(f"{self.player_name} You Win!")

        elif self.the_input < self.comp_num:
            print("%s Try higher!" % (self.player_name))

        elif self.the_input > self.comp_num:
            print("%s Try lower!" % (self.player_name))

player = input("What's your name?")
this_game = Guess_game(player)

while not this_game.game_over:
    '''Main loop for the game'''
    guess = int(input("Please guess a number"))
    this_game.check_game_over(guess)
    #get guess for this turn
    #increment number of goes
    #check whether too high or too low, display relevant message
    #check whether game over - either they got it right, or they've had 3 incorrect guesses. Call check_game_over()

#display correct message depending on whether they won or lost

