from sensob import ReflectanceSensob
from sensob import UltrasonicSensob


class Behaviour:

    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.sensobs = []
        self.motor_recoms = []
        self.halt_request = False
        self.priority = 0
        self.match_degree = 0
        self.active_flag = False
        self.weight = self.match_degree * self.priority

    def consider_deactivation(self):
        return

    def consider_activation(self):
        return

    def update(self):
        return

    def sense_and_act(self):
        return


class FollowLine(Behaviour):

    def __init__(self, bbcon):
        super(FollowLine, self).__init__(bbcon)
        self.r_sensob = ReflectanceSensob()
        self.sensobs.append(self.r_sensob)
        self.treshold = 0.3

    def consider_activation(self):
        """for value in self.r_sensob.update():
                    if value < self.treshold:
                        self.bbcon.activate_behaviour(self)
                        self.active_flag = True
                        return

                # deactivating
                self.weight = 0
                self.bbcon.deactivate_behaviour(self)
                self.active_flag = False"""

        if not self.active_flag:
            self.bbcon.activate_behaviour(self)
            self.active_flag = True
        return



    def consider_deactivation(self):
        self.consider_activation()

    def update(self):
        self.consider_activation()
        self.sense_and_act()
        self.weight = self.priority * self.match_degree

    def sense_and_act(self):
        self.r_sensob.update()

        if self.r_sensob.get_value()[1] < self.treshold:
            self.motor_recoms = ["L", 50]
            self.match_degree = 0.8

        elif self.r_sensob.get_value()[4] < self.treshold:
            self.motor_recoms = ["R",50]
            self.match_degree = 0.8

        else:
            self.motor_recoms = ["F", 50]
            self.match_degree = 0.5

        self.priority = 0.5

# stopper roboten hvis ultrasonic sensor oppdater noe nærmere enn 7cm
class Obstruction(Behaviour):

    # legger til sensob i oppførsel
    def __init__(self, bbcon):
        super(Obstruction, self).__init__(bbcon)
        self.u_sensob = UltrasonicSensob()
        self.sensobs.append(self.u_sensob)

    # aktiverer oppførsel hvis noe er nærmere enn 7 cm
    def consider_activation(self):
        if self.u_sensob.get_value() < 7:
            self.bbcon.activate_behaviour(self)
            self.active_flag = True
            self.halt_request = True

    # deaktiverer oppførsel hvis noe er lenger unna enn 7 cm
    def consider_deactivation(self):
        if self.u_sensob.get_value() > 7:
            self.bbcon.deactivate_behaviour(self)
            self.active_flag = False
            self.halt_request = False

    # oppdaterer oppførsel
    def update(self):
        for sensor in self.sensobs:
            sensor.update()

        # hvis aktiv, sjekker om oppførsel bør deaktiveres
        if self.active_flag:
            self.consider_deactivation()

        # hvis deaktiv, sjekk om oppførsel bør aktiveres
        elif not self.active_flag:
            self.consider_activation()

        # hvis deaktiv, sett vekt = 0
        if not self.active_flag:
            self.weight = 0
            return

        self.sense_and_act()
        self.weight = self.priority * self.match_degree

    def sense_and_act(self):
        self.motor_recoms = ["S", 500]
        self.priority = 1
        self.match_degree = 1






