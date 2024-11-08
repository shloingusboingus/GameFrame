#enemy projectile
from GameFrame import RoomObject, Globals
import random

class BONETROUSEL(RoomObject):
    
    def __init__(self, room, x, y):

        # attributaries of room object
        RoomObject.__init__(self,room, x, y)
        
        # set image
        image = self.load_image("AE.png")
        self.set_image(image,25,25)
        
        # set travel direction
        self.set_direction(90, 5)

        
        self.register_collision_object("babum")
        

    def step(self):
        self.outside_of_room()
        
    def outside_of_room(self):
        if self.x + self.width < 0:
            print("Bullet redirected into american school")
            self.room.delete_object(self)
            
    def handle_collision(self, other, other_type):        
        if other_type == "babum":
            Globals.next_level = Globals.levels.index('Starter')
            #stop this level so it goes to the next
            self.room.running = False