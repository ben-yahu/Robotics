from robot_control_class import RobotControl

rc = RobotControl()

all_LaserData = rc.get_laser_full()

count = 0
for value in all_LaserData:
    if value > count:
        count = value

print(f'The Highest Value is {value}')