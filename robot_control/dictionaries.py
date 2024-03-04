from robot_control_class import RobotControl

rc = RobotControl()

rclist = rc.get_laser_full()

rcdict = {
    'Position 0': rclist[0],
    'Position 100': rclist[100],
    'Position 200': rclist[200],
    'Position 300': rclist[300],
    'Position 400': rclist[400],
    'Position 500': rclist[500],
    'Position 600': rclist[600],
    'Position 719': rclist[719]
}

print(rcdict)