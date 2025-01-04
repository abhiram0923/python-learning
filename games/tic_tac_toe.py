import random

#Defining a class called Board. This would be initialize a 3x3 two dimensional array
#mimicing a tic tac toe game.
class Board:
  def __init__(self):
    self.board = [['_' for _ in range(3)] for _ in range(3)]
  def move(self, row, col, player):
    if self.is_valid_move(row, col):
      self.board[row][col] = player.name
      return True
    return False
  def is_valid_move(self, row, col):
    if 0 <= row <= 2 and 0 <= col <= 2:
      return self.board[row][col] == "_"
    return False
  def is_full(self):
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == "_":
          return False
    return True
  def display(self):
    for i in range(3):
      for j in range(3):
        print(self.board[i][j], end=" ")
      print()
  def is_there_a_winner(self):
    for i in range(3):
      if self.board[i][0] != "_" \
            and self.board[i][0] == self.board[i][1] == self.board[i][2]:
        return self.board[i][0]
    for i in range(3):
      if self.board[0][i] != "_" \
          and self.board[0][i] == self.board[1][i] == self.board[2][i]:
        return self.board[0][i]
    if self.board[0][0] != "_" \
          and self.board[0][0] == self.board[1][1] == self.board[2][2]:
      return self.board[0][0]
    if self.board[0][2] != "_" \
          and self.board[0][2] == self.board[1][1] == self.board[2][0]:
      return self.board[0][2]
    return None

#This is class that defines a player. 
#We also defined a method called get_move, which would prompt the user to enter a row/col selection.
class Player:
  def __init__(self, name):
    self.name = name
  def set_name(self,name):
    self.name=name
  def get_name(self):
    return self.name
  def get_move(self):
    row_prompt="Player {}, Enter Row: ".format(self.name)
    row = int(input(row_prompt))
    col_prompt="Player {}, Enter Column: ".format(self.name)
    col = int(input(col_prompt))
    return row,col

class Tic_Tac_Toe:
  def __init__(self):
    self.board = Board()
    self.player1 = Player("X")
    self.player2 = Player("O")
    self.current_player = random.choice([self.player1,self.player2])
    self.winner = None
  def switch_player(self):
    if self.current_player == self.player1:
      self.current_player = self.player2
    else:
      self.current_player = self.player1
  def check_winner(self):
    self.winner = self.board.is_there_a_winner()

  def play(self):
    while self.board.is_full() is False and self.winner is None:
      while True:
        row,col = self.current_player.get_move()
        if self.board.move(row,col,self.current_player) is True:
          break
        print("Invalid Move. Please Try again")
      self.board.display()
      self.switch_player()
      self.check_winner()
    print("The Winner is {}".format(self.winner))
    
def main():
  print("Playing Tic Tac Toe!")
  tic_tac_toe = Tic_Tac_Toe()
  tic_tac_toe.board.display()
  tic_tac_toe.play()
  

if __name__ == "__main__":
  main()
