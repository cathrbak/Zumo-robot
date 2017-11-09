from bbcon import BBCON
from behaviour import FollowLine, Obstruction
from zumo_button import ZumoButton

def main():

    bbcon = BBCON()
    follow_line = FollowLine(bbcon)
    obstruction = Obstruction(bbcon)


    bbcon.add_behaviour(follow_line)
    bbcon.add_behaviour(obstruction)
    print("before button")
    ZumoButton().wait_for_press()
    print("after button")
    while True:
        bbcon.run_one_timestep()

main()
