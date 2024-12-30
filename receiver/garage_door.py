class GarageDoor:

    def __init__(self, location):
        self.location = location

    def up(self):
        print(f"{self.location} garage door is up")

    def down(self):
        print(f"{self.location} garage door is down")

    def stop(self):
        print(f"{self.location} garage door is stopped")

    def light_on(self):
        print(f"{self.location} garage light is on")
    
    def light_off(self):
        print(f"{self.location} garage light is off")

    