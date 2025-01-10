from command.command import Command
from receiver.tv import TV

class TVOffCommand(Command):

    def __init__(self, tv: TV):
        self.tv = tv

    def undo(self):
        self.tv.on()
    
    def execute(self):
        self.tv.off()

    def __call__(self):
        self.execute()