from command.command import Command

class NoCommand(Command):
    def execute(self):
        pass

    def __call__(self):
        pass