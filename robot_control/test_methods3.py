from robot_control_class import RobotControl

rc = RobotControl(robot_name= 'summit')

def move_forward():
    a = rc.move_straight_time('forward', 0.3, 5)
    print(a)
    
def turn_clockwise():
    a = rc.turn('clockwise', 0.3, 7)
    print(a)

move_forward()

turn_clockwise()

