from arbitrator import Arbitrator
from motob import Motob

class BBCON:

    def __init__(self):
        self.behaviours = []        # liste med alle oppførslene til bbcon
        self.active_behaviours = []     # liste med alle oppførsler som er aktive
        self.sensobs = []       # liste med alle sensorobejekt brukt av bbcon
        self.motobs = Motob()        # liste med alle motorobjekt brukt av bbcon
        self.arbitrator = Arbitrator()   # ikke laget ennå

    # legger til en oppførsel
    def add_behaviour(self, behaviour):
        if behaviour not in self.behaviours:
            self.behaviours.append(behaviour)

    # legger til en sensor
    def add_sensob(self, sensob):
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)

    # legger til en oppførsel i aktivert-listen
    def activate_behaviour(self, behaviour):
        if behaviour in self.behaviours:
            self.active_behaviours.append(behaviour)

    # fjerner en aktiv oppførsel fra listen
    def deactivate_behaviour(self, behaviour):
        if behaviour in self.active_behaviours:
            self.active_behaviours.remove(behaviour)

    # kjerneaktiviteten til bbcon
    def run_one_timestep(self):

        # oppdaterer oppførsler som også oppdaterer sensobs
        for behaviour in self.behaviours:
            behaviour.update()

        # returnerer
        print("Active behaviours: ", self.active_behaviours)
        motor_recoms = self.arbitrator.choose_action(self.active_behaviours)

        # oppdaterer motobs
        self.motobs.update(motor_recoms)

        # reseter sensorverdier
        for sensor in self.sensobs:
            sensor.reset()



