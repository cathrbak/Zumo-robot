from bbcon import BBCON
from random import random as random


class Arbitrator:

    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        # Henter inn behaviours, velger behaviour tilfeldig ut ifra hver weight
        behaviours = self.bbcon.behaviours
        total_weight = sum(b.weight for b in behaviours)
        random_number = random(total_weight)

        w = total_weight
        for behaviour in behaviours:
            w -= behaviour.weight
            if random_number >= w:
                return behaviour.motor_recommendations, behaviour.halt_request
