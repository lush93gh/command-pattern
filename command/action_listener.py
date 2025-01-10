from abc import ABC, abstractmethod
from receiver.action_event import ActionEvent

class ActionListener(ABC):
    """
    ActionListener is the Command 
    Interface: it has one method, 
    actionPerformed() that, like 
    execute(), is executed when the 
    command is invoked.
    """
    
    @abstractmethod
    def action_performed(self, event: ActionEvent):
        pass
