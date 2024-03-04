from robot_control_class import RobotControl

rc = RobotControl()

laser1 = rc.get_laser(255)

print(f'Laser 1: {laser1}')

laser2 = rc.get_laser(528)

print(f'Laser 2: {laser2}')

laser2 = rc.get_laser(120)

print(f'Laser 3: {laser2}')
