from bbcon import BBCON
from random import random as random


class Arbitrator:

    def __init__(self):
        self.bbcon = BBCON()

    def choose_action(self):
        # Henter inn behaviours, velger behaviour tilfeldig ut ifra hver weight
        behaviors = self.bbcon.behaviors
        total_weight = sum(b.weight for b in behaviors)
        random_number = random(total_weight)

        w = total_weight
        for behavior in behaviors:
            w -= behavior.weight
            if random_number >= w:
                return behavior.motor_recommendations, behavior.halt_request
