#gameplay room :|
from GameFrame import Level
from Objects.UltimateFriskus import babum
from Objects.ismettatonWOKEnow import metatito

class Game(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("mm.png")

        # add HEART (player)
        self.add_room_object(babum(self, 600, 745))
        
        # add metatito (top row)
        self.add_room_object(metatito(self, 500, 50))
        self.add_room_object(metatito(self, 585, 50))
        self.add_room_object(metatito(self, 670, 50))
        self.add_room_object(metatito(self, 755, 50))
        

        # add metatito (middle row)
        self.add_room_object(metatito(self, 450, 110))
        self.add_room_object(metatito(self, 535, 110))
        self.add_room_object(metatito(self, 620, 110))
        self.add_room_object(metatito(self, 705, 110))
        self.add_room_object(metatito(self, 790, 110))


        # add metatito (bottom row)
        self.add_room_object(metatito(self, 340, 170))
        self.add_room_object(metatito(self, 465, 170))
        self.add_room_object(metatito(self, 550, 170))
        self.add_room_object(metatito(self, 640, 170))
        self.add_room_object(metatito(self, 730, 170))
        self.add_room_object(metatito(self, 830, 170))
