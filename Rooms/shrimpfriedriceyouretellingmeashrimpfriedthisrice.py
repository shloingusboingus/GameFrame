#starter window
from GameFrame import Level
from Objects.momifrewup import Title
from Objects.ohmeme import creditounbuttono
from Objects.STARRTT import START
from Objects.whydoyouhateme import GOAWAY

class shrimpfriedriceyouretellingmeashrimpfriedthisrice(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        #background image
        self.set_background_image("meow.gif")
        
        #word objects 
        self.add_room_object(Title(self, 140, 0))

        self.add_room_object(START(self, 500, 300))

        self.add_room_object(creditounbuttono(self, 525, 500))

        self.add_room_object(GOAWAY(self, 550, 650))