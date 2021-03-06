import numpy as np

size = 9
sqr_size = 3

def is_position_possible(tab, x, y, val):
  #vertical
  for i in range(size):
    if tab[x][i] == val:
      return False
 
  #horizontal
  for j in range(size):
    if tab[j][y] == val:
      return False
  
  #3x3 squares
  px = x // sqr_size
  py = y // sqr_size
  for k in range(sqr_size):
    for l in range(sqr_size):
      if tab[px*sqr_size + k][py*sqr_size + l] == val:
        return False
  
  return True

def solve_sudoku(tab):
  for i in range(size):
    for j in range(size):
      if tab[i][j] == 0:
        for v in range(1, 10):
          if(is_position_possible(tab, i, j, v)):
            tab[i][j] = v
            solve_sudoku(tab)
            tab[i][j] = 0
        return
  print('Solved\n', ':', np.matrix(tab))



sudoku = [
[8,0,0,0,0,0,0,0,0],
[0,0,3,6,0,0,0,0,0],
[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],
[0,0,0,0,4,5,7,0,0],
[0,0,0,1,0,0,0,3,0],
[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],
[0,9,0,0,0,0,4,0,0]
]

solve_sudoku(sudoku)
