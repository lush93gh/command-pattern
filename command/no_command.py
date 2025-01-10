from command.command import Command

class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass

    def __call__(self):
        pass

    def __str__(self):
        return self.__class__.__name__