import sys
import pygame

class Setting():
    #Класс для хранения всех настроек игры

    def __init__(self):
        #инициализируем настройки игры

        #параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (250,250,250)

        #настройки корабля
        #self.ship_speed = 1.5
        self.ship_limit = 3

        #параметр снаряда
        #self.bullet_speed = 5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        #настройки пришельцев
        #self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction = 1 - движение вправо, = -1 - движение влево
        self.fleet_direction = 1

        #темп ускорения игры
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        #инициализирую настройки, изменяющиеся в ходе игры
        self.ship_speed_factor = 2.5
        self.bullet_speed_factor = -2.0
        self.alien_speed_factor = 1.0

        self.ship_speed = self.alien_speed_factor
        self.bullet_speed = self.bullet_speed_factor
        self.alien_speed = self.alien_speed_factor

    def increase_speed(self):
        #увеличиваем настрйоки скорости
        self.ship_speed_factor *= self.speedup_scale 
        self.bullet_speed_factor *= self.speedup_scale 
        self.alien_speed_factor *= self.speedup_scale
        
        self.ship_speed = self.alien_speed_factor
        self.bullet_speed = self.bullet_speed_factor
        self.alien_speed = self.alien_speed_factor