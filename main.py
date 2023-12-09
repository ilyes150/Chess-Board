import pygame , sys
from const import *
from game import *
class Main:
    def __init__(self) :
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDHT,HEIGHT) )
        pygame.display.set_caption('chess')
        self.game = board()
    def mainloop(self):
        screen = self.screen
        game = self.game
        while True:
            game.show_bg(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
main = Main()
main.mainloop()