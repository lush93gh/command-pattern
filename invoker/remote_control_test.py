import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from invoker.simple_remote_control import SimpleRemoteControl
from receiver.light import Light
from receiver.garage_door import GarageDoor
from command.light_on_command import LightOnCommand
from command.garage_door_open_command import GarageDoorOpenCommand

class RemoteControlTest:
    """
    This is our Client in Command Pattern.
    """
    def test_light_on():
        # The remote is our Invoker; 
        # it will be passed a command 
        # object that can be used to 
        # make requests.
        remote = SimpleRemoteControl()
        # The Receiver of the request.
        light = Light()
        # Create a command and pass the Receiver to it. 
        light_on = LightOnCommand(light)
        # Pass the command to the Invoker.
        remote.set_command(light_on)
        # Simulate the button being pressed.
        remote.button_was_pressed()

    def test_garage_door_open():
        remote = SimpleRemoteControl()
        garage_door = GarageDoor()
        garage_open = GarageDoorOpenCommand(garage_door)
        remote.set_command(garage_open)
        remote.button_was_pressed() 

if __name__ == "__main__":
    RemoteControlTest.test_light_on()
    # RemoteControlTest.test_garage_door_open()
