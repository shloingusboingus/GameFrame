from GameFrame import RoomObject, Globals
import random

class BONETROUSEL(RoomObject):
    
    def __init__(self, room, x, y):

        # attributaries of room object
        RoomObject.__init__(self,room, x, y)
        
        # set image
        image = self.load_image("AE.png")
        self.set_image(image,50,49)

        
        # set travel direction
        angle = random.randint(135,225)
        self.set_direction(angle, 10)
        

    def step(self):
        self.keep_in_room()
        self.outside_of_room()
        
    def keep_in_room(self):
        if self.x < 380:
            self.x = 380
            self.x_speed *= -1
        elif self.x > 880:
            self.x = 880
            self.x_speed *= -1
            
    def outside_of_room(self):
        if self.x + self.width < 0:
            print("Bullet redirected into american school")
            self.room.delete_object(self)