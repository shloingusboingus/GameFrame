#speed buff

from GameFrame import RoomObject

class mania(RoomObject):
    
    def __init__(self,room,x,y):
        # include attirbutes and method from RoomObject
        RoomObject.__init__(self,room,x,y)
        
        # set image
        image = self.load_image("sweetie.png")
        self.set_image(image,50,49)
        
        # set travel direction
        self.set_direction(90, 5)
        
        # handle events
        self.register_collision_object("babum")

        
    def step(self):
        self.outside_of_room()
        
    # --- Event Handlers
    def handle_collision(self, other, other_type):
        # ship collision
        if other_type == "babum":
            self.room.delete_object(self)
            
    def outside_of_room(self):
        if self.x + self.width < 0:
            self.room.delete_object(self)