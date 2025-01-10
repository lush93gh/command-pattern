from command.action_listener import ActionListener
from receiver.action_event import ActionEvent

class AngelListener(ActionListener):

    def action_performed(self, event: ActionEvent):
        # The Receiver in this example is the System object. 
        # Invoking a command results in actions on 
        # the Receiver. In a typical Swing application this would 
        # result in calling actions on other components in the UI.

        print("Don't do it, you might regret it!")