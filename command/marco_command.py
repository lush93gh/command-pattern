from command.command import Command

class MarcoCommand(Command):
    """
     A Command that can execute other Commands.
    """
    
    def __init__(self, commands: list[Command]):
        """
        Take an array of Commands and store them in the MacroCommand.
        """
        self.commands = commands

    def execute(self):
        """
        When the macro gets executed, execute those commands one at a time.
        """
        for command in self.commands:
            command.execute()

    def undo(self):
        # TODO
        pass

    def __call__(self):
        self.execute()

    def __str__(self):
        return self.__class__.__name__