from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        """
        All we need is one method call execute().
        """
        pass