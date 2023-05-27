class Setting:
    #сдесь все файлы игры
    def __init__(self):
        #экран
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #корабль
        self.ship_speed = 2
        self.ship_limit = 3
        #Патрон
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 1

        #пришелец
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        #fleet_direction = 1 - движение вправо
        self.fleet_direction = 1

        self.speedup_scale = 1.2
        self.initiali_dynamic_settings()

    def initiali_dynamic_settings(self):
        self.ship_speed_factor = 2.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.ship_speed = self.ship_speed_factor
        self.bullet_speed = self.bullet_speed_factor
        self.alien_speed = self.alien_speed_factor

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.ship_speed = self.ship_speed_factor
        self.bullet_speed = self.bullet_speed_factor
        self.alien_speed = self.alien_speed_factor








