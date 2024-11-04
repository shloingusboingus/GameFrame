#Title object thingy

from GameFrame import RoomObject

class Title(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # make the image
        image = self.load_image("skittle.png")
        self.set_image(image,1000,250)


