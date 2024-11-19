#hud ig
from GameFrame import TextObject, Globals, RoomObject

class dun(TextObject):

    def __init__(self, room, x: int, y: int, text=None):
    
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()
        
    def dundundun(self, change):
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()
        

class Livvy(RoomObject):
    def __init__(self, room, x: int, y: int):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        self.livvy_icon = []
        # load the various lives images into a live list
        for index in range(6):
            self.livvy_icon.append(self.load_image(f"cunk.png"))
        self.update_image()
        
        
    def update_image(self):
        self.set_image(self.livvy_icon[Globals.LIVES], 125, 23)


class derogatory(RoomObject):
    def __init__(self, room, x: int, y: int):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        self.derogatory_icon = []
        # load the various lives images into a live list
        for index in range(6):
            self.derogatory_icon.append(self.load_image(f"cunk.png"))
        self.update_image()
        
    def update_image(self):
        self.set_image(self.derogatory_icon[Globals.ENEMY_LIVES], 125, 230)