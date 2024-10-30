#le start button 

from GameFrame import RoomObject

class START(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("unstartito.jpg")
        self.set_image(image,300,150)


