#player!!!
from GameFrame import RoomObject, Globals
import pygame

#BIRTH OF A GOD
class babum(RoomObject):
    
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # make player image 
        image = self.load_image("mlub.png")
        self.set_image(image,45,45)
        
        # register events
        self.handle_key_events = True

#MOVE  
    def key_pressed(self, key):

        
        if key[pygame.K_LEFT]:
            self.x -= 50
        elif key[pygame.K_RIGHT]:
            self.x += 50


#BORDERS
    def keep_in_room(self):
       
        if self.x < 380:
            self.x = 380
        elif self.x > 880:
            self.x = 880

    def step(self):
        self.keep_in_room()