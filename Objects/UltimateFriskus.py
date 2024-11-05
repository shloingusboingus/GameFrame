#player!!!
from GameFrame import RoomObject, Globals
import pygame

class babum(RoomObject):
    
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # make player image 
        image = self.load_image("mlub.png")
        self.set_image(image,45,45)
        
        # register events
        self.handle_key_events = True
        
    def key_pressed(self, key):

        if key[pygame.K_a]:
            self.x -= 10
        elif key[pygame.K_d]:
            self.x += 10

    def keep_in_room(self):
       
        if self.x < 400:
            self.x = 400
        elif self.x + self.height> Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.height
        
        if self.x < -880:
            self.x = 880
        elif self.x + self.height> Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.height

    def step(self):
        self.keep_in_room()