class Stereo():

    def __init__(self, location: str):
        self.location = location
        self.volume = 0

    def on(self):
        print(f"{self.location} stereo is on")

    def off(self):
        print(f"{self.location} stereo is off")

    def set_cd(self):
        print(f"{self.location} stereo is set for CD input")

    def set_dvd(self):
        print(f"{self.location} stereo is set for DVD input")

    def set_radio(self):
        print(f"{self.location} stereo is set for radio input")

    def set_volume(self, volume):
        self.volume = volume
        print(f"{self.location} stereo volume set to {self.volume}")

    def __str__(self):
        return self.location + " stereo"