from bbcon import BBCON
from behaviour import FollowLine
from zumo_button import ZumoButton

def main():

    bbcon = BBCON()
    follow_line = FollowLine(bbcon)

    bbcon.add_behaviour(follow_line)

    ZumoButton().wait_for_press()

    while True:
        bbcon.run_one_timestep()

main()
