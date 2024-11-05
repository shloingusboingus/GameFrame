#player!!!
from GameFrame import RoomObject
import pygame

class babum(RoomObject):
    
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # make frisk 
        image = self.load_image("mlub.png")
        self.set_image(image,50,50)
        
        # register events
        self.handle_key_events = True
        
    def key_pressed(self, key):

        
        if key[pygame.K_a]:
            self.x_speed -= 10
        elif key[pygame.K_d]:
            self.x_speed += 10

            