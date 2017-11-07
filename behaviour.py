from sensob import ReflectanceSensob

class Behaviour:

    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.sensobs = []
        self.motor_recoms = []
        self.active_flag = False
        self.halt_request = False
        self.priority = 0
        self.match_degree = 0
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
        for value in self.r_sensob.update():
            if value < self.treshold:
                self.bbcon.active_behaviour(self)
                self.activate_flag = True
                return

        # deactivating
        self.weight = 0
        self.bbcon.deactivate_behaviour(self)
        self.active_flag = False

    def consider_deactivation(self):
        self.consider_activation()

    def update(self):
        self.consider_activation()
        self.sense_and_act()
        self.weight = self.priority * self.match_degree

    def sense_and_act(self):
        self.r_sensob.update()

        if self.r_sensob.getValue()[1] < self.treshold:
            self.motor_recoms = ["L", 50]
            self.match_degree = 0.8

        elif self.r_sensob.getValue()[4] < self.treshold:
            self.motor_recoms = ["R", 50]
            self.match_degree = 0.8

        else:
            self.motor_recoms = ["F", 50]
            self.match_degree = 0.5

        self.priority = 0.5





