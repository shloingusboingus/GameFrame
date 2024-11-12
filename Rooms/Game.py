#gameplay room :|
from GameFrame import Level
from Objects.UltimateFriskus import babum
from Objects.ismettatonWOKEnow import metatito
from Objects.METAphysics import metatitoo
from Objects.METAmonstrosities import metatitooo

class Game(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("mm.png")

        # add HEART (player)
        self.add_room_object(babum(self, 600, 745))
        
        # add metatitoo (top row)
        self.add_room_object(metatitooo(self, 500, 50))
        self.add_room_object(metatitooo(self, 585, 50))
        self.add_room_object(metatitooo(self, 670, 50))
        self.add_room_object(metatitooo(self, 755, 50))
        

        # add metatitoo (upper middle row)
        self.add_room_object(metatitoo(self, 350, 110))
        self.add_room_object(metatitoo(self, 465, 110))
        self.add_room_object(metatitoo(self, 550, 110))
        self.add_room_object(metatitoo(self, 640, 110))
        self.add_room_object(metatitoo(self, 730, 110))
        self.add_room_object(metatitoo(self, 830, 110))
        


        # add metatito (middle row)
        self.add_room_object(metatito(self, 340, 170))
        self.add_room_object(metatito(self, 465, 170))
        self.add_room_object(metatito(self, 550, 170))
        self.add_room_object(metatito(self, 640, 170))
        self.add_room_object(metatito(self, 730, 170))
        self.add_room_object(metatito(self, 830, 170))

           # add metatito (lower middle row)
        self.add_room_object(metatito(self, 340, 230))
        self.add_room_object(metatito(self, 465, 230))
        self.add_room_object(metatito(self, 550, 230))
        self.add_room_object(metatito(self, 640, 230))
        self.add_room_object(metatito(self, 730, 230))
        self.add_room_object(metatito(self, 830, 230))


        # add metatito (lower middle row)
        self.add_room_object(metatito(self, 340, 290))
        self.add_room_object(metatito(self, 465, 290))
        self.add_room_object(metatito(self, 550, 290))
        self.add_room_object(metatito(self, 640, 290))
        self.add_room_object(metatito(self, 730, 290))
        self.add_room_object(metatito(self, 830, 290))

        # add metatito (bottom row)
        self.add_room_object(metatito(self, 340, 170))
        self.add_room_object(metatito(self, 465, 170))
        self.add_room_object(metatito(self, 550, 170))
        self.add_room_object(metatito(self, 640, 170))
        self.add_room_object(metatito(self, 730, 170))
        self.add_room_object(metatito(self, 830, 170))
