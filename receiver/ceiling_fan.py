class CeilingFan():
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, location: str):
        """
        The CeilingFan instance holds local state representing 
        the speed of the ceiling fan.
        """
        self.location = location
        self.speed = CeilingFan.OFF

    def high(self):
        self.speed = CeilingFan.HIGH
        print(f"{self.location} ceiling fan is on high")

    def medium(self):
        self.speed = CeilingFan.MEDIUM
        print(f"{self.location} ceiling fan is on medium")

    def low(self):
        self.speed = CeilingFan.LOW
        print(f"{self.location} ceiling fan is on low")

    def off(self):
        self.speed = CeilingFan.OFF
        print(f"{self.location} ceiling fan is off")

    def get_speed(self):
        """
        Get the current speed of the ceiling fan.
        """
        return self.speed
    
    def __str__(self):
        return self.location + " ceiling fan"