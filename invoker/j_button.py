from receiver.action_event import ActionEvent
from command.action_listener import ActionListener

class JButton:

    def __init__(self, text: str):
        self.text = text
        self.action_listeners: list[ActionListener] = []

    def add_action_listener(self, action_listener):
        self.action_listeners.append(action_listener)

    def action_performed(self, event: ActionEvent):
       for action_listener in self.action_listeners:
           action_listener.action_performed(event)
