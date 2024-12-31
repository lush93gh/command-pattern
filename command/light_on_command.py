from command.command import Command
from receiver.light import Light

class LightOnCommand(Command):
    """
    Implement the Command interface.
    """
    def __init__(self, light: Light):
        """
        The constructor is passed the specific 
        light that this command is going to 
        control—say the living room light—
        and stashes it in the light instance 
        variable. When execute gets called, 
        this is the light object that is going 
        to be the receiver of the request.
        """
        self.light = light

    def execute(self):
        """
        Calls the on() method on the 
        receiving object, which is 
        the light we are controlling.
        """
        self.light.on()

    def undo(self):
        """
        Turn the light back off.
        """
        self.light.off()
    
    def __call__(self):
        self.execute()
