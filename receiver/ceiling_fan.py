class CeilingFan():

    def __init__(self, location):
        self.location = location
        self.speed = 0

    def high(self):
        self.speed = 3
        print(f"{self.location} ceiling fan is on high")

    def medium(self):
        self.speed = 2
        print(f"{self.location} ceiling fan is on medium")

    def low(self):
        self.speed = 1
        print(f"{self.location} ceiling fan is on low")

    def off(self):
        self.speed = 0
        print(f"{self.location} ceiling fan is off")

    def get_speed(self):
        return self.speed
    
    def __str__(self):
        return self.location + " ceiling fan"
    