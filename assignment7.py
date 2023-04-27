import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return self.name

class Die:
    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

class PigGame:
    def __init__(self, players):
        self.players = players
        self.current_player = players[0]
        self.other_player = players[1]
        self.die = Die()

    def switch_players(self):
        self.current_player, self.other_player = self.other_player, self.current_player

    def take_turn(self):
        turn_score = 0

        decision = input(f"{self.current_player}, Press r to roll ")
        if (decision == "r"):
            while(decision == "r"):
                roll = self.die.roll()
                if (roll == 1):
                        print(f"{self.current_player}, you rolled a 1! You get no points this turn and your turn ends.")
                        return
                turn_score += roll
                print(f"{self.current_player}, you rolled a {roll}! Your current turn score is {turn_score} and your total score is {self.current_player.score}.")
                decision = input("Do you want to roll again (r) or hold (h)? ")
                if(decision != "h" and decision != "r"):
                    print("Invalid input, try either 'r' or 'h'")
        
        if(decision == "h"):
            self.current_player.score += turn_score
            print(f"{self.current_player}, your turn has ended. Your total score is now {self.current_player.score}.")
            return  
        if(decision != "h" and decision != "r"):
            print("Invalid input, try either 'r' or 'h'")

            

        
        

    def play(self):
        print(f"Welcome to Pig, {self.players[0]} and {self.players[1]}!")

        while True:
            self.take_turn()
            if self.current_player.score >= 100:
                print(f"Congratulations, {self.current_player}! You won!")
                break
            self.switch_players()




player1 = Player("Alice")
player2 = Player("Bob")

game = PigGame([player1, player2])
game.play()