# Initial and Imports
import pygame
import numpy as np
from solver import *
white, black, red, grey = (255,255,255), (0,0,0), (255,0,0), (200, 200, 200)
pygame.init()
font = pygame.font.SysFont('Comic Sans', 25)

### Sudoku board ###
class board:
     
     ## Initialize ##
     def __init__(self):
          self.rect_size = 50
          self.H = 450
          self.W = 450
          self.focus_tile = (0,0)
          self.initial_board = np.array([[3, 7, 8, 0, 2, 9, 4, 0, 5],
                                         [0, 0, 9, 0, 0, 1, 7, 6, 0],
                                         [0, 6, 0, 0, 4, 0, 0, 0, 8],
                                         [0, 0, 0, 1, 8, 0, 0, 9, 0],
                                         [0, 0, 2, 0, 0, 4, 0, 5, 7],
                                         [0, 0, 6, 0, 0, 7, 0, 0, 0],
                                         [0, 1, 0, 2, 0, 0, 5, 0, 0],
                                         [0, 0, 7, 0, 0, 0, 0, 0, 1],
                                         [9, 0, 0, 0, 1, 0, 6, 7, 0]])
     
          self.board = np.copy(self.initial_board)
          # create screen
          self.screen = self.initialize_screen()
          # draw initial board
          self.initialize_board()
          
          
     # Create initial pygame screen
     def initialize_screen(self):
          screen = pygame.display.set_mode((self.H,self.W))
          pygame.display.set_caption("Sudoku")
          screen.fill(white)
          return screen
     
     # Draw initial board
     def initialize_board(self):
          # Draw (9x9) tiles
          for x in range(9):
               for y in range(9):
                    # Draw tile
                    self.draw_tile(x, y)
         
     # Draw (x, y) tile: background, border and number
     def draw_tile(self, x, y):
          # Reset Tile
          self.draw_rect(x, y, white)
          
          # Fill grey if initial
          if self.is_tile_initial(x, y):
               self.draw_rect(x, y, grey)
          
          # Draw border (red if focused)
          if self.is_tile_focused(x, y):
               self.draw_rect_border(x, y, red)
          else:
               self.draw_rect_border(x, y, black)
          
          # Draw number
          self.draw_num_in_tile(x, y)
          
     # Draw num in tile (x,y)
     def draw_num_in_tile(self, x, y):
          # Ignore drawing 0
          if self.board[y][x]!=0:
               # Draw position
               pos_x = (x*self.rect_size)+(self.rect_size/2.6)
               pos_y = (y*self.rect_size)+(self.rect_size/2.6)
               
               # Render num to print
               num = font.render(str(self.board[y][x]), 1, black)
               self.screen.blit(num, (pos_x, pos_y))
          
     # Detect number input to focused tile
     def input_num(self, num):
          x = self.focus_tile[0]
          y = self.focus_tile[1]
          # Only change num if wasnt on initial board
          if (self.is_tile_initial(x, y) == False):
               self.board[y][x] = num
               self.draw_tile(x, y)


     # on Mouse input: Move focus tile
     def input_click(self, pos):
          
          # Update focus tile
          prev_focus = self.focus_tile
          self.focus_tile = (int(pos[0]/self.rect_size), int(pos[1]/self.rect_size))
          
          # Re-draw previous and new focus tiles
          self.draw_tile(prev_focus[0], prev_focus[1])
          self.draw_tile(self.focus_tile[0], self.focus_tile[1])
          

     ### Helper Functions ###
     
     # draw rectangle in (x,y) pos
     def draw_rect(self, x, y, color):
          pos_x = x * self.rect_size
          pos_y = y * self.rect_size
          pygame.draw.rect(self.screen, color, [pos_x, pos_y, self.rect_size,self.rect_size])
          
     # draw rectangle border in (x,y) pos
     def draw_rect_border(self, x, y, color):
          pos_x = x * self.rect_size
          pos_y = y * self.rect_size
          pygame.draw.rect(self.screen, color, [pos_x, pos_y, self.rect_size,self.rect_size], 2)
          
     # Tile is on initial_board
     def is_tile_initial(self, x, y):
         return (self.initial_board[y][x]!=0)
    
     # Tile is in focus
     def is_tile_focused(self, x, y):
          return ((x,y) == self.focus_tile)
     
     
     #### Solver ###
     def solver(self):
          self.board = np.copy(self.initial_board)
          rec_solver(self, 0, 0)
          








