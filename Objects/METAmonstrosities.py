#metamonstrosities
#third row enemy
# This enemy will drop speed firing speed boosts at the at the player upon death

from GameFrame import RoomObject, Globals
import random
from Objects.metagun import BONETROUSEL
from Objects.Sweetheart import mania

#la alphys put ghost in robot
class metatitooo(RoomObject):

    def __init__(self, room, x, y):

        #le roomobject attributaries 
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("metatit.webp")
        self.set_image(image,75,50)

        # collision with player

         # set movement
        self.set_direction(90, 0.1)
        #self.y_speed = random.choice([-10,10])
        
    def keep_in_room(self):
        if self.x < 380:
            self.x = 380
        elif self.x > 880:
            self.x = 880
          #if self.x < 380 or self.x > 880 - self.width:
           # self.x_speed *= -1
            
    def step(self):
        #self.keep_in_room()
        self.outside_of_room()

                   
    def handle_collision(self, other, other_type):
        print(other_type)     
        if other_type == "Lovecraft":
            buffy_wuffy_uwu = mania(self.room, self.x, self.y)
            print("buffy wuffy uwu")
            self.room.add_object(buffy_wuffy_uwu)
            self.room.delete_object(self)

    def outside_of_room(self):
        if self.y + self.height > Globals.SCREEN_HEIGHT:
            print("byyyyyeeeee")
            self.room.delete_object(self)
            Globals.next_level = Globals.levels.index('Starter')
            self.room.running = False
    
         # create buff
    def createbuff(self):
        if metatitooo.register_collision_object("Lovecraft"):
           speed_buff = mania(self.room, self.x, self.y)