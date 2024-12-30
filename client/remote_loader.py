import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from invoker.remote_control import RemoteControl
from receiver.light import Light
from receiver.ceiling_fan import CeilingFan
from receiver.stereo import Stereo
from command.stereo_on_with_cd_command import StereoOnWithCDCommand

class RemoteLoader():
    """
    The RemoteLoader creates a number of Command objects 
    that are loaded into the slots of the Remote Control. Each 
    command object encapsulates a request of a home 
    automation device. 
    """

    def load():
        remote_control = RemoteControl()

        # Create all the devices in their proper locations.
        living_room_light = Light("Living Room")
        kitchen_light = Light("Kitchen")
        ceiling_fan = CeilingFan("Living Room")
        stereo = Stereo("Living Room")

        # Create the stereo On and Off commands.
        stereo_on_with_cd = StereoOnWithCDCommand(stereo, volume = 11)

        # Load all the commands into the remote slots.
        remote_control.set_command(str(living_room_light), living_room_light.on, living_room_light.off)
        remote_control.set_command(str(kitchen_light), kitchen_light.on, kitchen_light.off)
        remote_control.set_command(str(ceiling_fan), ceiling_fan.high, ceiling_fan.off)
        remote_control.set_command(str(stereo), stereo_on_with_cd.execute, stereo.off)

        # Here’s where we use our __str__() method 
        # to print each remote slot and the command 
        # assigned to it.
        # Note that __str__() gets 
        # called automatically here, so we don’t have 
        # to call __str__() explicitly.
        print(remote_control)

        # Step through each slot and push its On and Off buttons.
        remote_control.on_button_was_pushed(str(living_room_light))
        remote_control.off_button_was_pushed(str(living_room_light))
        remote_control.on_button_was_pushed(str(kitchen_light))
        remote_control.off_button_was_pushed(str(kitchen_light))
        remote_control.on_button_was_pushed(str(ceiling_fan))
        remote_control.off_button_was_pushed(str(ceiling_fan))
        remote_control.on_button_was_pushed(str(stereo))
        remote_control.off_button_was_pushed(str(stereo))

if __name__ == "__main__":
    RemoteLoader.load()

