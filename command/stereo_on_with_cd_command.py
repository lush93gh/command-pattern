from command.command import Command
from receiver.stereo import Stereo

class StereoOnWithCDCommand(Command):

    def __init__(self, stereo: Stereo, volume):
        """
        1. Pass the instance of the stereo 
        we’re going to be controlling and 
        store it in an instance variable.
        2. Store the volume in an instance variable,
        rather than hardcoding it.
        """
        self.stereo = stereo
        self.volume = volume
        self.__name__ = "Stereo On With CD Command"

    def execute(self):
        """
        To carry out this request, we need to call three 
        methods on the stereo: first, turn it on, then set 
        it to play the CD, and finally set the volume.
        """
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(self.volume)

    def __call__(self):
        self.execute()