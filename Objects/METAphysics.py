#second row enemy
# This enemy will fire at the player, but are destroyed more easily than others

from GameFrame import RoomObject, Globals
import random
from Objects.metagun import BONETROUSEL
import random

#la alphys put ghost in robot
class metatitoo(RoomObject):

    def __init__(self, room, x, y):

        #le roomobject attributaries 
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("metatit.webp")
        self.set_image(image,75,50)

        # set up the bullet spawn timer
        gatling_bullet_spawn_time = random.randint(10,150)
        self.set_timer(gatling_bullet_spawn_time, self.bulletito)

        # collision with player
        self.register_collision_object("babum")

         # set movement
        self.set_direction(90, 0.5) 
        #self.y_speed = random.choice([-10,10])
        
    def keep_in_room(self):
        if self.x < 380:
            self.x = 380
        elif self.x > 880:
            self.x = 880
          #if self.x < 380 or self.x > 880 - self.width:
           # self.x_speed *= -1
            
    def step(self):
        self.keep_in_room()
        self.outside_of_room()
        
    def outside_of_room(self):
        if self.y + self.height > Globals.SCREEN_HEIGHT:
            print("byyyyyeeeee")
            self.room.delete_object(self)
            Globals.next_level = Globals.levels.index('Starter')
            self.room.running = False


        # PULL THE LEVER KRONK
    def bulletito(self):
        
        #birth of the darkness
        new_bulletito = BONETROUSEL(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_bulletito)
        
        #WRONG LEVEEERR
        gatling_bullet_spawn_time = random.randint(150, 200)
        self.set_timer(gatling_bullet_spawn_time, self.bulletito)

    def handle_collision(self, other, other_type):        
        if other_type == "babum":
            Globals.next_level = Globals.levels.index('Starter')
            #stop this level so it goes to the next
            self.room.running = False