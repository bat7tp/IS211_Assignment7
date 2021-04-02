import random
import argparse
import time

class Player:
    def __init__(self, name_player):
        self.name_player = name_player
        self.score_total = 0
        self.turn_total = 0

class ComputerPlayer(Player):

    def decide(self):

        if self.turn_total > min(25, 100 - self.score_total):
            # self.score_total += self.turn_total
            # self.turn_total = 0
            return 'h'
        else:
            return 'r'


class PlayerFactory:

    def create(self, player_type):
        if player_type == "computer":
            computer = ComputerPlayer("Robot")
            return computer
        elif player_type == "human":
            player = Player("Batsheva")
            return player
        else:
            print("Not an acceptable input")
            return 0


class Dice:

    def roll_die(self):

        #random.seed(0)
        number_rolled = random.randint(1, 6)
        return number_rolled

class Game:

    def start(self, player1type, player2type):

        dice = Dice()

        player_factory = PlayerFactory()
        player1 = player_factory.create(player1type)
        player2 = player_factory.create(player2type)
        # player1 = Player("Batsheva")
        # player2 = Player("Elan")

        current_player = player1

        while player1.score_total < 100 and player2.score_total < 100:
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1

            current_player.turn_total = 0
            print(current_player.name_player)
            while True:
                print("This is your current turn total: " + str(current_player.turn_total))
                print("This is your current game total: " + str(current_player.score_total))

                if isinstance(current_player, ComputerPlayer):
                    decision = current_player.decide()
                else:
                    decision = input("Do you want to roll? Press r. Do you want to hold? Press h.")

                if decision == 'r':
                    what_was_rolled = dice.roll_die()
                    if what_was_rolled >=2 and what_was_rolled <=6:
                        print("Nice. You rolled a", what_was_rolled, "That number will be added to your total score.")
                        current_player.turn_total += what_was_rolled
                    if what_was_rolled == 1:
                        current_player.turn_total = 0
                        print("You rolled a 1. Your turn is over. You have", current_player.score_total, "points. Next player please go.")
                        break


                if decision == 'h':
                    current_player.score_total += current_player.turn_total
                    print("Okay. Turn held. Your score as of now is: " + str(current_player.score_total))
                    break


        #print("The game is over.")

class Timed_Game_Proxy:

    def __init__(self):
        self.proxy_timer = Game()

    def timer_start(self, player1type, player2type):
        start = time.time()

        dice = Dice()

        player_factory = PlayerFactory()
        player1 = player_factory.create(player1type)
        player2 = player_factory.create(player2type)
        # player1 = Player("Batsheva")
        # player2 = Player("Elan")

        current_player = player1

        while player1.score_total < 100 and player2.score_total < 100:
            #print("hello")
            current_time = time.time()
            print("current time is: " + str(current_time))
            print("start time is: " + str(start))
            print("time elapsed: " + str(current_time - start))

            if current_time - start >= 60:
                print("Time is up. Game over")
                break

            if current_player == player1:
                current_player = player2
            else:
                current_player = player1

            current_player.turn_total = 0
            print(current_player.name_player)
            while True:
                print("This is your current turn total: ", str(current_player.turn_total))
                print("This is your current game total: ", str(current_player.score_total))

                if isinstance(current_player, ComputerPlayer):
                    decision = current_player.decide()
                else:
                    decision = input("Do you want to roll? Press r. Do you want to hold? Press h.")

                if decision == 'r':
                    what_was_rolled = dice.roll_die()
                    if what_was_rolled >=2 and what_was_rolled <=6:
                        print("Nice. You rolled a", what_was_rolled, "That number will be added to your total score.")
                        current_player.turn_total += what_was_rolled
                    if what_was_rolled == 1:
                        current_player.turn_total = 0
                        print("You rolled a 1. Your turn is over. You have", current_player.score_total, "points. Next player please go.")
                        break


                if decision == 'h':
                    current_player.score_total += current_player.turn_total
                    print("Okay. Turn held. Your score as of now is: ")
                    print(str(current_player.score_total))
                    break



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='This decides if computer or human will be playing'
    )

    parser.add_argument('--player1', required=True)
    parser.add_argument('--player2', required=True)
    parser.add_argument('--timer', required=True)

    args = parser.parse_args()

    if args.timer == 'True':
        #print("truth")
        game = Timed_Game_Proxy()
        game.timer_start(args.player1, args.player2)
    else:
        #print("falseee")
        game = Game()
        game.start(args.player1, args.player2)




