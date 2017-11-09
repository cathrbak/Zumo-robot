from random import random as random


class Arbitrator:

    def __init__(self, randomchoice=False):
        self.randomchoice=randomchoice

    def choose_action(self, behaviours):
        if self.randomchoice:
            # Velger behaviour tilfeldig ut ifra hver weight

            total_weight = sum(b.weight for b in behaviours)
            random_number = random()*total_weight

            w = total_weight
            for behaviour in behaviours:
                w -= behaviour.weight
                if random_number >= w:
                    return behaviour.motor_recoms, behaviour.halt_request
        else:
            hi = -1
            temp = None
            for behaviour in behaviours:
                if behaviour.weight > hi:
                    hi = behaviour.weight
                    temp = behaviour
            if temp:
                return temp.motor_recoms, temp.halt_request
