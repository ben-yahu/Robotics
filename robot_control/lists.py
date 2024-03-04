from robot_control_class import RobotControl

rc = RobotControl()

rclist = rc.get_laser_full()

print(f'At Position 0: {rclist[0]}\nAt Position 360: {rclist[360]}\nAt Position 719: {rclist[719]}\n')