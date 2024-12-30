from command.command import Command

class StereoOffCommand(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()