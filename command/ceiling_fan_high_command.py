from command.command import Command
from receiver.ceiling_fan import CeilingFan

class CeilingFanHighCommand(Command):

    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan
        # Local state to keep track of the previous speed of the fan.
        self.prev_speed = ceiling_fan.get_speed()
    
    def execute(self):
        """
        Before we change the speed of the 
        fan, we need to first record its previous state, 
        just in case we need to undo our actions.
        """
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()

    def undo(self):
        """
        Set the speed of the fan back to its previous speed.
        """
        if self.prev_speed == CeilingFan.HIGH:
            self.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.off()

    def __call__(self):
        self.execute()
