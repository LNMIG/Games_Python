from random import choice


##### SUBRUTINES #########################################################################################

def enter_move(board, move):
      # This function accpets the board and the movement/selection made by the player,
      # checks the data and updates the board if required.
      if 0 <= move <= 8:
          aux = move
          row = aux // 3
          column = aux % 3

      if board[row][column] not in ['O', 'X']:
          board[row][column] = 'O'
          return True
      else:
          return False


def make_list_of_free_fields(board):
      # This function returns a list with numbers indicating emptiness of the squares in the board.
      global free_squares
      free_squares = [ (i*3 + j) for i in range(3) for j in range(3) if board[i][j] not in ['O','X'] ]
      return free_squares


def victory_for(board):
      # This function analyze the board'status in order to verify if 
      # the player that uses 'O's or 'X's is the winner.
      draw = make_list_of_free_fields(board)

      rows_O = [True for i in range(3) if board[i].count('O') == 3]
      rows_X = [True for i in range(3) if board[i].count('X') == 3]
      columns_O = [True for i in range(3) for j in range(1) if board[j][i] == board[j+1][i] == board[j+2][i] == 'O']
      columns_X = [True for i in range(3) for j in range(1) if board[j][i] == board[j+1][i] == board[j+2][i] == 'X']
      cross1_O =  [True if board[0][0] == board[1][1] == board[2][2] == 'O' else None]
      cross2_O =  [True if board[0][2] == board[1][1] == board[2][0] == 'O' else None]
      cross1_X =  [True if board[0][0] == board[1][1] == board[2][2] == 'X' else None]
      cross2_X =  [True if board[0][2] == board[1][1] == board[2][0] == 'X' else None]

      state_O = [rows_O, columns_O, cross1_O, cross2_O]
      state_X = [rows_X, columns_X, cross1_X, cross2_X]

      for each in state_O:
          if len(each) > 0 and each[0]:
            return 'user'
      for each in state_X:
          if len(each) > 0 and each[0]:
            return 'program'
      if len(draw) == 0:
          return 'draw'
      return 'go-on'


def draw_move(board):
      # This function updates the board using program's choice/move.
      move = choice(free_squares)
      row = move // 3
      column = move % 3
      board[row][column] = 'X'

##########################################################################################################


##### MAIN development and FINAL resut ###################################################################

def run(board, move):
      isUserMoveOk = enter_move(board, move)
      results = victory_for(board)

      if isUserMoveOk and results == 'go-on':
          draw_move(board)
          results = victory_for(board)

          if results == 'go-on':
              finished = ''
              return (board, finished)
          elif results == 'program':
              finished = '¡¡  Program WINS  !!'
              return (board, finished)
          else:
              finished = '¡¡ Draw, no winner !!'
              return (board, finished)

      if isUserMoveOk and results == 'user':
          finished = '¡¡  User WINS  !!'
          return (board, finished)

##########################################################################################################