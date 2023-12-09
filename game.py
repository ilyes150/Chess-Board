import pygame
from const import *
class board:
    def __init__(self) :
        pass
    def show_bg(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col)%2==0:
                    color = (255,255,255)
                else :
                    color = (0,0,128)
                rect = (col * SQSIZE, row * SQSIZE , SQSIZE,SQSIZE)
                pygame.draw.rect(surface,color,rect)