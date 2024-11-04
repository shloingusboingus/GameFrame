#le start button 

from GameFrame import RoomObject, Globals

class Startbutton(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("unstartito.jpg")
        self.set_image(image,300,150)

        self.handle_mouse_events = True

    def clicked(self, button_number):
        if button_number == 1:
            #sets the next level to whatever the text is in the index section
            Globals.next_level = Globals.levels.index('Game')
            #stop this level so it goes to the next
            self.room.running = False
            print("next level")


