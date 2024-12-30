from abc import ABC, abstractmethod

class Command(ABC):
    """
    All RemoteControl commands implement the Command interface, 
    which consists of one method: execute(). 
    Commands encapsulate a set of actions on a specific vendor class. 
    The remote invokes these actions by calling the execute() method.
    """

    @abstractmethod
    def execute(self):
        """
        All we need is one method call execute().
        """
        pass

    @abstractmethod
    def __call__(self):
        pass