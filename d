import sys
import pygame



class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('ИНОПЛАНЕТНОЕ ВТОРЖЕНИЕ')
        self.bg_color = (230,230,230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip(self.bg_color)

if __name__ == '__main__':
    aw = AlienInvasion()
    aw.run_game
