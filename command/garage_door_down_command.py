from command.command import Command

class GarageDoorDownCommand(Command):

    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()