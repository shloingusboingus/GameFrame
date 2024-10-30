#gameplay room :|

from GameFrame import Level

class tralala(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("ihatethis.png")