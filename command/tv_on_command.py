from command.command import Command
from receiver.tv import TV

class TVOnCommand(Command):

    def __init__(self, tv: TV):
        self.tv = tv

    def undo(self):
        self.tv.off()
    
    def execute(self):
        self.tv.on()

    def __call__(self):
        self.execute()