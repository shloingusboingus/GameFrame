#THE LEAVE BUTTON

from GameFrame import RoomObject, Globals

class Leavebutton(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("whywouldyouleave.jpg")
        self.set_image(image,200,100)

#le mouse click 
        self.handle_mouse_events = True
    def clicked(self, button_number):
        if button_number == 1:
            exit()

