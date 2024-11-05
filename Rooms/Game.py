#gameplay room :|
from GameFrame import Level
from Objects.UltimateFriskus import babum

class Game(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("mm.png")

        # add HEART
        self.add_room_object(babum(self, 25, 50))