from ultrasonic import Ultrasonic
from reflectance_sensors import ReflectanceSensors
from camera import Camera
from basic_robot import zumo_button

class Sensob:

    def __init__(self):
        self.sensors = []
        self.value = None

    def get_value(self):
        return self.value

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()


    def update(self):
        return


class UltrasonicSensob(Sensob):

    def __init__(self):
        super(UltrasonicSensob, self).__init__()
        self.sensor = Ultrasonic()
        self.sensors.append(self.sensor)

    def get_value(self):
        ''' returnerer en verdi = avstand i cm'''
        return self.value

    def update(self):
        self.sensor.update()
        self.value = self.sensor.get_value()
        return self.value


class ReflectanceSensob(Sensob):

    def __init__(self):
        super(ReflectanceSensob, self).__init__()
        self.sensor = ReflectanceSensors()
        self.sensors.append(self.sensor)

    def get_value(self):
        ''' returnerer en liste med verdier: [left, midleft, midright right]'''
        return self.value

    def update(self):
        self.sensor.update()
        self.value = self.sensor.get_value()
        return self.value


class CameraSensob(Sensob):

    def __init__(self):
        super(CameraSensob, self).__init__()
        self.sensor = Camera()
        self.sensors.append(self.sensor)

    def get_value(self):
        return self.sensor.value

    def update(self):
        ''' Returnerer verdi som RGB-array'''
        self.sensor.update()
        self.value = self.sensor.get_value()
        return self.value

