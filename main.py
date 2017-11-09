
from bbcon import BBCON
from behaviour import FollowLine

def main():

    bbcon = BBCON()
    follow_line = FollowLine(bbcon)

    bbcon.add_behaviour(follow_line)

    while True:
        bbcon.run_one_timestep()

main()
