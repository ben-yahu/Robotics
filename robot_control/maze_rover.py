from robot_control_class import RobotControl
import time
rc = RobotControl()

class Rover:
    def __init__(self, direction, time = 3.1):
        if direction == 'Left':
            self.direction = 719
        if direction == 'Right':
            self.direction = 0
        if direction == 'Front':
            self.direction = 360
        if direction == 'Back':
            self.direction = 180
        if direction == 'Full':
            self.direction = [360, 719, 0, 180]
        self.time = time

    def check_loc(self):
        loc_list = {}
        direction_map = {1 : 'Front', 2 : 'Back', 3 : 'Right', 4 : 'Left'}
        if isinstance(self.direction, list):
            for i in self.direction:
                if i == 360:
                    key = 'Front'
                elif i == 719:
                    key = 'Left'
                elif i == 0:
                    key = 'Right'
                elif i == 180:
                    key = 'Back'
                loc_list[key] = round(rc.get_laser(i), 2)
        else:
            key = direction_map.get(user_inp)
            loc_list[key] = round(rc.get_laser(self.direction), 2)


        return loc_list

    def move_rover(self):
        while rc.get_laser(360) > 1:
            rc.move_straight()
            start_time = 0
            if time.time() - start_time >= 10:
                rc.stop_robot()
        rc.stop_robot()
        a = rc.get_laser(0)
        b = rc.get_laser(719)

        print('Right', a)
        print('Left', b)

    def turn_rover(self):
        a = rc.get_laser(0)
        b = rc.get_laser(719)

        print('Right', a)
        print('Left', b)
        if a > b:
            while rc.get_laser(360) < 4:
                rc.rotate(-24)
            rc.stop_robot()

        elif a < b:
            while rc.get_laser(360) < 4:
                rc.rotate(24)
            rc.stop_robot()

user_inp = int(input('Which Position do u want to see?\n1. Front\n2. Back\n3. Right\n4. Left\n5. All\n\n'))
if user_inp == 1:
    r1 = Rover('Front')
if user_inp == 2:
    r1 = Rover('Back')
if user_inp == 3:
    r1 = Rover('Right')
if user_inp == 4:
    r1 = Rover('Left')
if user_inp == 5:
    r1 = Rover('Full')

val = r1.check_loc()
print(val)

move_rov = str(input('Shall we move the Robot?\nY or N\n\n'))
if move_rov.lower() == 'y':
    while rc.get_laser(0) > 0.1 and rc.get_laser(719) > 0.1 and rc.get_laser(360) > 0.1:
        r1.move_rover()
        r1.turn_rover()
else:
    print('Robot Stopped!')

# cd /home/user/catkin_ws/src/robot_control
# python maze_rover.py