from command.command import Command
from receiver.hottub import Hottub

class HottubOnCommand(Command):

    def __init__(self, hottub: Hottub):
        self.hottub = hottub

    def undo(self):
        self.hottub.off()
    
    def execute(self):
        self.hottub.on()

    def __call__(self):
        self.execute()
