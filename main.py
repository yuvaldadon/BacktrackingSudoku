# Initial and Imports
import pygame
import numpy as np
from solver import *
from board import *

#### Main Program ###
                    
# Init board
obj = board()
pygame.display.update()

# Beginning of game
gameExit = False
while not gameExit:
     # update screen
     pygame.display.flip()
     
     # User inputs
     for event in pygame.event.get():
          # Quit on exit click
          if event.type == pygame.QUIT:
               gameExit = True
               
          # Get mouse clicks and move focus tile
          if event.type == pygame.MOUSEBUTTONUP:
               pos = pygame.mouse.get_pos()
               obj.input_click(pos)
               print(obj.focus_tile)
               
                    
          # Get number inputs
          if event.type == pygame.KEYDOWN:
               # number keys
               if event.key in range(49,58): # 0-9 are 48-57 as input code
                    num = event.key-48
                    obj.input_num(num)
                    print(event.key-48)
                    
               # numpad keys
               if event.key >= pygame.K_KP1 and event.key <= pygame.K_KP9:
                    num = event.key-pygame.K_KP1+1
                    obj.input_num(num)
                    print(num)
                    
               # delete keys
               if (event.key == pygame.K_DELETE) or (event.key == pygame.K_BACKSPACE):
                    num = 0
                    obj.input_num(num)
                    
               # initiate solver with F1
               if (event.key == pygame.K_F1):
                    obj.solver()
               
#quit from pygame & python
pygame.quit()
