import pygame.font

class Buttom():
    def __init__(self,ai_game,msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width,self.height = 200, 50
        self.buttom_color = (55,155,190)
        self.text_color = (60,255,85)
        self.font = pygame.font.SysFont(None,48)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        #сообщение кнопки создается только один раз!
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.buttom_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def drow_buttom(self):
        self.screen.fill(self.buttom_color, self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)