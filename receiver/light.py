class Light:

    def __init__(self, location: str):
        self.location = location

    def on(self):
        print(f"{self.location} light is on")

    def off(self):
        print(f"{self.location} light is off")

    def __str__(self):
        return self.location + " light"