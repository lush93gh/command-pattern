class Hottub:
    
    def __init__(self):
        self.temperature = 98

    def on(self):
        self.set_temperature(104)
        self.circulate()

    def off(self):
        self.set_temperature(98)

    def circulate(self):
        print("Hottub is bubbling!")
    
    def jets_on(self):
        print("Hottub jets is on")

    def jets_off(self):
        print("Hottub jets is off")

    def set_temperature(self, temperature):
        if self.temperature < temperature:
            print(f"Hottub is heating to a steaming {temperature} degrees")
        else:
            print(f"Hottub is cooling to {temperature} degrees")

        self.temperature = temperature

    def __str__(self):
        return Hottub.__name__