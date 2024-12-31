from command.command import Command
from command.no_command import NoCommand

class RemoteControlWithUndo:
    no_command: Command = NoCommand()

    def __init__(self):
        self.on_commands: dict[Command] = {}
        self.off_commands: dict[Command] = {}
        # Stash the last command executed for the undo button.
        # Just like the other slots, undo starts off with a noCommand, 
        # so pressing undo before any other button won’t do anything at all
        self.last_command = RemoteControlWithUndo.no_command

    def set_command(self, slot: str, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: str):
        """
        When a button is pressed, we take 
        the command and first execute 
        it; then we save a reference to 
        it in the last_command instance variable.
        """
        self.on_commands.get(slot, RemoteControlWithUndo.no_command).execute()
        self.last_command = self.on_commands.get(slot, RemoteControlWithUndo.no_command)
    
    def off_button_was_pushed(self, slot: str):
        """
        When a button is pressed, we take 
        the command and first execute 
        it; then we save a reference to 
        it in the last_command instance variable.
        """
        self.off_commands.get(slot, RemoteControlWithUndo.no_command).execute()
        self.last_command = self.off_commands.get(slot, RemoteControlWithUndo.no_command)

    def undo_button_was_pushed(self):
        """
        When the undo button is pressed, we 
        invoke the undo() method of the 
        command stored in last_command. 
        This undoes the operation of the last 
        command executed.
        """
        self.last_command.undo()

    def __str__(self):
        string = "\n------ Remote Control -------\n"
        for i, (on_command, off_command) in enumerate(zip(self.on_commands.values(), self.off_commands.values())):
            string += f"[slot {i}] {on_command.__class__.__name__}   {off_command.__class__.__name__}\n"
            string += f"[undo] {self.last_command.__class__.__name__}\n"
        return string