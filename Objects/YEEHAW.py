#player projectile 

from GameFrame import RoomObject, Globals
from Objects.Sweetheart import mania

class Lovecraft(RoomObject):
    
    def __init__(self, room, x, y):
        # attributaries of room object
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("magical.png")
        self.set_image(image, 9, 33)
        
        # direction
        self.set_direction(270, 5)

        #collision with enemy targets/enemy projectiles
        self.register_collision_object("metatito")
        self.register_collision_object("metatitoo")
        self.register_collision_object("metatitooo")
        #self.register_collision_object("BONETROUSEL")
        
    def step(self):
        self.outside_of_room()
        
    def outside_of_room(self):           
        if self.y > Globals.SCREEN_HEIGHT:
            self.room.delete_object(self)

            
    #  event handlers
    def handle_collision(self, other, other_type):
        if other_type == "metatito" or "metatitoo" or "metatitooo":
            if other_type == "metatitooo":
                buffy_wuffy_uwu = mania(self.room, self.x, self.y)
                print("buffy wuffy uwu")
                self.room.add_room_object(buffy_wuffy_uwu)
            self.room.delete_object(self)
            self.room.delete_object(other)
            self.room.delete_object(self)