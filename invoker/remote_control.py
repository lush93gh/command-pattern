from command.command import Command
from command.no_command import NoCommand

class RemoteControl:
    """
    The RemoteControl class manages a set of Command objects, one per button. 
    When a button is pressed, the corresponding button_was_pushed() method 
    is called, which invokes the execute() method on the command. 
    That is the full extent of the remote’s knowledge of the classes it’s invoking 
    as the Command object decouples the remote from the classes doing the actual home automation work.
    """
    no_command: Command = NoCommand()

    def __init__(self):
        """
        1. The remote is going to handle seven On and Off commands, 
        which we’ll hold in corresponding dicts.
        2. In the constructor, all we need to 
        do is instantiate and initialize the 
        On and Off dicts.
        """
        self.on_commands: dict[Command] = {}
        self.off_commands: dict[Command] = {}

    def set_command(self, slot: str, on_command: Command, off_command: Command):
        """
        1. The set_command() method takes a slot 
        position and an On and Off command to 
        be stored in that slot. 
        2. It puts these commands in the 
        On and Off dicts for later use.
        """
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: str):
        """
        When an On button is 
        pressed, the hardware takes 
        care of calling the on_button_was_pushed().
        """
        self.on_commands.get(slot, self.no_command)()
    
    def off_button_was_pushed(self, slot: str):
        """
        When an Off button is 
        pressed, the hardware takes 
        care of calling the off_button_was_pushed().
        """
        self.off_commands.get(slot, self.no_command)()

    def __str__(self):
        """
        We override __str__() to print out each slot and 
        its corresponding command. You’ll see us use this 
        when we test the remote control. 
        """
        string = "\n------ Remote Control -------\n"
        for i, (on_command, off_command) in enumerate(zip(self.on_commands.items(), self.off_commands.items())):
            string += f"[slot {i}] {on_command[0]} {on_command[1].__name__}   {off_command[0]} {off_command[1].__name__}\n"
        return string