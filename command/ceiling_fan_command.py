from command.command import Command
from receiver.ceiling_fan import CeilingFan


class CeilingFanCommand(Command):

    def __init__(self, ceiling_fan: CeilingFan, speed: int):
        self.ceiling_fan = ceiling_fan
        # Local state to keep track of the previous speed of the fan.
        self.prev_speed = ceiling_fan.get_speed()
        self.speed = speed

    def execute(self):
        """
        Before we change the speed of the
        fan, we need to first record its previous state,
        just in case we need to undo our actions.
        """
        self.prev_speed = self.ceiling_fan.get_speed()
        self._set_speed(self.speed)

    def undo(self):
        """
        Set the speed of the fan back to its previous speed.
        """
        self._set_speed(self.prev_speed)

    def _set_speed(self, speed: int):
        if speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif speed == CeilingFan.OFF:
            self.ceiling_fan.off()

    def _get_speed_from_int(self, speed: int) -> str:
        return (
            "High"
            if speed == CeilingFan.HIGH
            else (
                "Medium"
                if speed == CeilingFan.MEDIUM
                else (
                    "Low"
                    if speed == CeilingFan.LOW
                    else "Off" if speed == CeilingFan.OFF else ""
                )
            )
        )

    def __call__(self):
        self.execute()

    def __str__(self):
        return f"CeilingFan{self._get_speed_from_int(self.speed)}Command"
