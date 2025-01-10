import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from invoker.remote_control import RemoteControl
from invoker.remote_control_with_undo import RemoteControlWithUndo
from receiver.light import Light
from receiver.ceiling_fan import CeilingFan
from receiver.stereo import Stereo
from receiver.tv import TV
from receiver.hottub import Hottub
from command.light_on_command import LightOnCommand
from command.light_off_command import LightOffCommand
from command.stereo_on_with_cd_command import StereoOnWithCDCommand
from command.stereo_on_command import StereoOnCommand
from command.stereo_off_command import StereoOffCommand
from command.tv_on_command import TVOnCommand
from command.tv_off_command import TVOffCommand
from command.hottub_on_command import HottubOnCommand
from command.hottub_off_command import HottubOffCommand
from command.ceiling_fan_command import CeilingFanCommand
from command.marco_command import MarcoCommand

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
        remote_control.set_command(str(stereo), stereo_on_with_cd, stereo.off)

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
    
    def load_with_undo():
        remote_control = RemoteControlWithUndo()

        # Create a Light.
        living_room_light = Light("Living Room")

        # Light In and Off Commands with undo() enabled().
        living_room_light_on = LightOnCommand(living_room_light)
        living_room_light_off = LightOffCommand(living_room_light)

        # Add the light Commands to the remote in slot.
        remote_control.set_command(str(living_room_light), living_room_light_on, living_room_light_off)

        # Turn the light on, then off, and then undo.
        remote_control.on_button_was_pushed(str(living_room_light))
        remote_control.off_button_was_pushed(str(living_room_light))
        print(remote_control)
        remote_control.undo_button_was_pushed()
        # Turn the light off, back on, and undo.
        remote_control.off_button_was_pushed(str(living_room_light))
        remote_control.on_button_was_pushed(str(living_room_light))
        print(remote_control)
        remote_control.undo_button_was_pushed()
        
    def load_ceiling_fan():
        remote_control = RemoteControlWithUndo()

        ceiling_fan = CeilingFan("Living Room")

        # Instantiate three commands: medium, high, and off.
        ceiling_fan_medium = CeilingFanCommand(ceiling_fan, speed = CeilingFan.MEDIUM)
        ceiling_fan_high = CeilingFanCommand(ceiling_fan, speed = CeilingFan.HIGH)
        ceiling_fan_off = CeilingFanCommand(ceiling_fan, speed = CeilingFan.OFF)

        # Put medium and high in slot. We also load up the off command.
        remote_control.set_command(str(ceiling_fan_medium), ceiling_fan_medium, ceiling_fan_off)
        remote_control.set_command(str(ceiling_fan_high), ceiling_fan_high, ceiling_fan_off)

        # Turn the light on, then off, and then undo.
        remote_control.on_button_was_pushed(str(ceiling_fan_medium))
        remote_control.off_button_was_pushed(str(ceiling_fan_medium))
        print(remote_control)
        remote_control.undo_button_was_pushed()
        # Turn the light off, back on, and undo.
        remote_control.on_button_was_pushed(str(ceiling_fan_high))
        print(remote_control)
        remote_control.undo_button_was_pushed()

    def load_macro_command():
        remote_control = RemoteControlWithUndo()

        # Create all the devices: a light, tv, stereo, and hot tub.
        light = Light("Living Room")
        tv = TV("Living Room")
        stereo = Stereo("Living Room")
        hottub = Hottub()

        # Create all the On commands to control them.
        light_on = LightOnCommand(light)
        stereo_on = StereoOnCommand(stereo)
        tv_on = TVOnCommand(tv)
        hottub_on = HottubOnCommand(hottub) 

        # TODO off buttons.
 
        # Create an array for On commands and an array for Off commands.
        party_on = [light_on, stereo_on, tv_on, hottub_on]
        party_off = [light_off, stereo_off, tv_off, hottub_off]

        # Create two corresponding macros to hold commands.
        party_on_macro = MarcoCommand(party_on)
        party_off_macro = MarcoCommand(party_off)

        # Assign the macro command to a button.
        remote_control.set_command(MarcoCommand.__name__, party_on_macro, party_off_macro)

        print(remote_control)
        print("--- Pushing Macro On---")
        remote_control.on_button_was_pushed(MarcoCommand.__name__)
        print("--- Pushing Macro Off---")
        remote_control.off_button_was_pushed(MarcoCommand.__name__)


if __name__ == "__main__":
    # RemoteLoader.load()
    # RemoteLoader.load_with_undo()
    # RemoteLoader.load_ceiling_fan()
    RemoteLoader.load_macro_command()

