#starter window
from GameFrame import Level
from Objects.Title import Title
from Objects.Creditbutton import Creditbutton
from Objects.Startbutton import Startbutton
from Objects.Leavebutton import Leavebutton

class Starter(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        #background image
        self.set_background_image("meow.gif")
        
        #word objects 
        self.add_room_object(Title(self, 140, 0))

        self.add_room_object(Startbutton(self, 500, 300))

        self.add_room_object(Creditbutton(self, 525, 500))

        self.add_room_object(Leavebutton(self, 550, 650))