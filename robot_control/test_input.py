from robot_control_class import RobotControl

rc = RobotControl()

user_Input = int(input('Enter a number between 0 and 719: '))

laser = rc.get_laser(user_Input)

print(f'Position {user_Input} value is: {laser}')