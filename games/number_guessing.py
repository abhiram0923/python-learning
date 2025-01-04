import random
class number_game:
  def __init__(self):
    self.number = self.generate_number()
    self.guesses = 0
  def generate_number(self):
    return random.randint(1,100)
  def check_guess(self, guess):
    if self.number == guess:
      print("Congrats! You guessed the right number.")
    elif guess < self.number:
      print("The number is low.")
    else:
      print("The number is high.")
  def play(self):
    print("Welcome to the number guessing game. Please guess a number between 1-100.")
    while True:
      x = int(input("Guess a nubmer between 1-100: "))
      self.check_guess(x)
      if self.number == x:
        break
      self.guesses+=1
      if self.guesses >= 6:
        print("Too many guesses, you loose the game.")
        break
      

game = number_game()
game.play()
    
