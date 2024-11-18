#speed buff
#genuinely could not for the life of me find a way for it to change anything, or generally interact with anything so i gave up on it to give me more time to do the rest of my game since i genuinely, wholeheartedly do not know how to code
#still spawns, just doesn't do nothing

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
            print("buff")

    def buff_effect(self, other, other_type):
        self.handle_collision(self, other, other_type)
        other.bopbopbop(
             other.set_timer(- 10, other.reload))
 


    def outside_of_room(self):
        if self.x + self.width < 0:
            self.room.delete_object(self)