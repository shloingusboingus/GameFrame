#credits button 

from GameFrame import RoomObject
import pygame

class Creditbutton(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("ohyeahallme.jpg")
        self.set_image(image,250,100)

#le mouse click 
