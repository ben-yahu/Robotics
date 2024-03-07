from robot_control_class import RobotControl

rc = RobotControl(robot_name = 'summit')

def move_forward(time = 2.5):
    a = rc.move_straight_time('forward', 0.7, time)
    print(a)

def turn_left():
    a = rc.turn('counter-clockwise', 0.6, 3)
    print(a)

move_forward()
turn_left()
move_forward()
turn_left()
move_forward(5)