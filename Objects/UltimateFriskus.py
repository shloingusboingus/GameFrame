#player!!!
from GameFrame import RoomObject, Globals
from Objects.YEEHAW import Lovecraft
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
 
        #projectile shoot
        self.can_shoot = True


#MOVE  
    def key_pressed(self, key):
        if key[pygame.K_LEFT]:
            self.x -= 5
        elif key[pygame.K_RIGHT]:
            self.x += 5
        if key[pygame.K_SPACE]:
            self.bopbopbop()


#BORDERS
    def keep_in_room(self):
        if self.x < 380:
            self.x = 380
        elif self.x > 880:
            self.x = 880

    def step(self):
        self.keep_in_room()

    def bopbopbop(self):
        if self.can_shoot:
            new_bullet = Lovecraft(self.room, 
                            self.x + self.height, 
                            self.y + self.width/2 - 4)
            self.room.add_room_object(new_bullet)
            self.can_shoot = False
            self.set_timer(18,self.reload)
            
    def reload(self):
        self.can_shoot = True