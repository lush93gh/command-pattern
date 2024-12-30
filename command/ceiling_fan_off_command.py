from command.command import Command
from receiver.ceiling_fan import CeilingFan

class CeilingFanOffCommand(Command):

    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan
    
    def execute(self):
        self.ceiling_fan.off()