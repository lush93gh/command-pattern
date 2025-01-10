class TV:
    DVD = "DVD"

    def __init__(self, location: str):
        self.location = location
        self.channel = TV.DVD
        self.volume = 0

    def on(self):
        print(f"{self.location} TV is on")
        print(f"{self.location} TV channel is set for {self.channel}")

    def off(self):
        print(f"{self.location} TV is off")

    def set_input_channel(self, channel):
        self.channel = channel
        print(f"{self.location} TV channel is set for {self.channel}")

    def set_volume(self, volume):
        self.volume = volume
        print(f"{self.location} TV volume set to {self.volume}")

    def __str__(self):
        return self.location + " TV"