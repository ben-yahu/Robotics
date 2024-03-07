from robot_control_class import RobotControl

rc = RobotControl(robot_name= 'summit')

class Square:
    def __init__(self, sq_time):
        self.sq_time = sq_time
    def sm_sq(self):
        a = rc.move_straight_time('forward', 0.7, self.sq_time)
        print(a)
        b = rc.turn('counter-clockwise', 0.6, 3)
        print(b)
        a = rc.move_straight_time('forward', 0.7, self.sq_time)
        print(a)
        b = rc.turn('counter-clockwise', 0.6, 3)
        print(b)
        a = rc.move_straight_time('forward', 0.7, self.sq_time)
        print(a)
        b = rc.turn('counter-clockwise', 0.6, 3)
        print(b)
        a = rc.move_straight_time('forward', 0.7, self.sq_time)
        print(a)
        print('Reached Destination')

    def bg_sq(self):
        a = rc.move_straight_time('forward', 0.7, 2 * self.sq_time)
        print(a)
        b = rc.turn('counter-clockwise', 0.6, 3)
        print(b)
        a = rc.move_straight_time('forward', 0.7, 2 * self.sq_time)
        print(a)
        b = rc.turn('counter-clockwise', 0.6, 3)
        print(b)
        a = rc.move_straight_time('forward', 0.7, 2 * self.sq_time)
        print(a)
        b = rc.turn('counter-clockwise', 0.6, 3)
        print(b)
        a = rc.move_straight_time('forward', 0.7, 2 * self.sq_time)
        print(a)
        print('Reached Destination')

sq1 = Square(2)

sq1.sm_sq()
sq1.bg_sq()