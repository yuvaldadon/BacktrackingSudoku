# Initial and Imports
import pygame
import numpy as np

#initial_board = np.array([[2, 0, 0, 0, 9, 3, 5, 0, 0],
#                         [1, 0, 0, 0, 0, 0, 3, 4, 0],
#                         [8, 0, 0, 5, 2, 0, 0, 0, 0],
#                         [0, 0, 0, 0, 0, 0, 0, 0, 3],
#                         [0, 9, 0, 2, 7, 0, 8, 0, 0],
#                         [7, 1, 8, 0, 3, 5, 9, 0, 6],
#                         [9, 8, 5, 6, 1, 0, 0, 3, 4],
#                         [0, 2, 0, 7, 4, 0, 6, 0, 0],
#                         [6, 0, 7, 3, 5, 8, 0, 0, 0]])
#board=np.copy(initial_board)

# Check if list has no duplicates in 1-9 range
def no_duplicates(list):
     temp=[]
     for i in list:
          if i!=0:
               if i in temp:
                    return False
               else:
                    temp.append(i)
     return True

# check if num is valid for tile
def num_checker(board, x, y):
     # check row
     if no_duplicates(board[y,:]) is False:
          return False
     # check column
     if no_duplicates(board[:,x]) is False:
          return False
     # check square
     square_x = x%3
     square_y = y%3
     square=board[square_x*3:square_x*3+3, square_y*3:square_y*3+3].reshape(-1) # shape square into a list
     if no_duplicates(square)is False:
          return False
     
     # valid entry if got here
     return True
     
     
#pseudo-code
def rec_solver(obj, x, y):
     # Move to next line
     if x==9:
          x=0;
          y+=1;
          
     # Finished recursion end condition
     if y==9:
          return True
     
     # Dont check if tile was in initial board
     if obj.is_tile_initial(x, y):
          return rec_solver(obj, x+1, y)
     
     # Check all numbers
     else:
          for i in range(1,10):
               # update board
               obj.board[y][x] = i
               obj.focus_tile = (x,y)
               
               # move focus and draw
               obj.draw_tile(x, y)
               
               # delay and display
               pygame.time.delay(1)
               pygame.display.flip()
               # If number is valid, attempt next tile in recursion
               if num_checker(obj.board, x, y):
                    # try next tile
                    obj.focus_tile = (-1,-1)
                    obj.draw_tile(x, y)
                    if rec_solver(obj, x+1, y):
                         return True
          
          # Return false if reached here and backtrack
          obj.focus_tile = (-1,-1)
          obj.draw_tile(x, y)
          obj.board[y][x] = 0
          return False
     
     
     