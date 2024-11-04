#gameplay room :|

from GameFrame import Level

class Game(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        print("Game")
        self.set_background_image("skittle.jpg")