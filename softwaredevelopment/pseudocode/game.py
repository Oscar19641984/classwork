import random

class game:
    def __init__(self, guess):
        self.guess = guess
    
    def random(self):
        self.number = random.randint(1,10)
        return self.number
    
    def validate(self, guess):
        if self.number == guess:
            print("You are right")
        else:
            print("You are wrong")

def main():
    guess = int(input("Enter your number: "))
    game1 = game(guess)
    game1.random()
    game1.validate(guess)
    play_again = input("Would you like to play again: ")
    while play_again.lower() == "yes":
        guess = int(input("Enter your number: "))
        game1 = game(guess)
        game1.random()
        game1.validate(guess)
        play_again = input("Would you like to play again: ")

main()