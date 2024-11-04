#THE LEAVE BUTTON

from GameFrame import RoomObject

class Leavebutton(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("whywouldyouleave.jpg")
        self.set_image(image,200,100)


