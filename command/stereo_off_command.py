from command.command import Command

class StereoOffCommand(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def undo(self):
        self.stereo.on()

    def execute(self):
        self.stereo.off()

    def __call__(self):
        self.execute()