import random


class Player:
    def __init__(self, name_player):
        self.name_player = name_player
        self.score_total = 0



class Dice:

    def roll_die(self):

        random.seed(0)
        number_rolled = random.randint(1, 6)
        return number_rolled

class GameSimulation:

    dice = Dice()


    player1 = Player("Batsheva")
    player2 = Player("Elan")

    current_player = player1

    while player1.score_total < 100 and player2.score_total < 100:
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

        turn_total = 0
        print(current_player.name_player)
        while True:
            print("This is your current turn total: ", str(turn_total))
            print("This is your current game total: ", str(current_player.score_total))
            decision = input("Do you want to roll? Press r. Do you want to hold? Press h.")

            if decision == 'r':
                what_was_rolled = dice.roll_die()
                if what_was_rolled >=2 and what_was_rolled <=6:
                    print("Nice. You rolled a", what_was_rolled, "That number will be added to your total score.")
                    turn_total += what_was_rolled
                if what_was_rolled == 1:
                    turn_total = 0
                    print("You rolled a 1. Your turn is over. You have", current_player.score_total, "points. Next player please go.")
                    break


            if decision == 'h':
                current_player.score_total += turn_total
                print("Okay. Turn held. Your score as of now is: ")
                print(str(current_player.score_total))
                break


    print("The game is over.")









