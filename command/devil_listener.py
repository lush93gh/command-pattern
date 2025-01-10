from command.action_listener import ActionListener
from receiver.action_event import ActionEvent

class DevilListener(ActionListener):

    def action_performed(self, event: ActionEvent):
        print("Come on, do it!")