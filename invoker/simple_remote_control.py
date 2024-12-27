from command.command import Command

class SimpleRemoteControl:
    def __init__(self):
        """
        We have one slot to hold our command, 
        which will control one device.
        """
        self.slot = None

    def set_command(self, command: Command):
        """
        We have a method for setting the 
        command the slot is going to control. 
        This could be called multiple times if the 
        client of this code wanted to change 
        the behavior of the remote button.
        """
        self.slot = command

    def button_was_pressed(self):
        """
        This method is called when the button 
        is pressed. All we do is take the 
        current command bound to the slot 
        and call its execute() method.
        """
        self.slot.execute()