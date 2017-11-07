from basic_robot.motors import Motors

class Motob:

    LEFT = "L"
    RIGHT = "R"
    FORWARDS = "F"
    BACKWARDS = "B"
    STOP = "S"

    def __init__(self):
        self.motor = Motors()
        self.value = None
        self.speed = 0.5

    def update(self, mr):
        # mottar en motor recommendation mr
        self.value = mr
        self.operationalize()

    def operationalize(self):
        # Gjør om mr til en motor setting, og mater det til motoren.
        action = self.value[0]
        value = self.value[1]

        if action == self.LEFT:
            self.motor.left(speed=self.speed, dur=value)
        elif action == self.RIGHT:
            self.motor.right(speed=self.speed, dur=value)
        elif action == self.FORWARDS:
            self.motor.forward(speed=self.speed, dur=value)
        elif action == self.BACKWARDS:
            self.motor.backward(speed=self.speed, dur=value)
        elif action == self.STOP:
            self.motor.stop()



