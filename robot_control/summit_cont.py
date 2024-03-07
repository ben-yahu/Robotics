from robot_control_class import RobotControl
import time

rc = RobotControl(robot_name = 'summit')

def move(m):
    rc.move_straight()
    time.sleep(m)
    rc.stop_robot()

def get_laser_val():
    a = [int(input(f'Enter a number (0 - 719):')) for _ in range(3)]
    first_Laser = rc.get_laser_summit(a[0])
    second_Laser = rc.get_laser_summit(a[1])
    third_Laser = rc.get_laser_summit(a[2])
    list_read = [first_Laser, second_Laser, third_Laser]
    return list_read

values = get_laser_val()
print(values)