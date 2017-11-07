
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



