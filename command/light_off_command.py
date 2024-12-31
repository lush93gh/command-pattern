from command.command import Command

class LightOffCommand(Command):
    """
    The LightOffCommand works exactly 
    the same way as the LightOnCommand, 
    except that we’re binding the receiver to 
    a different action: the off() method.
    """

    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.off()

    def undo(self):
        """
        Turn the light back on.
        """
        self.light.on()
    
    def __call__(self):
        self.execute()