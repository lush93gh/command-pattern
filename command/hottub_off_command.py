from command.command import Command
from receiver.hottub import Hottub

class HottubOffCommand(Command):

    def __init__(self, hottub: Hottub):
        self.hottub = hottub

    def undo(self):
        self.hottub.on()
    
    def execute(self):
        self.hottub.off()

    def __call__(self):
        self.execute()
