from robot_control_class import RobotControl

rc = RobotControl()

wall_Dist = rc.get_laser(360)

while wall_Dist > 1:
    rc.move_straight()
    wall_Dist = rc.get_laser(360)
    print(f'Wall at a distance of {wall_Dist:.2f}m')

rc.stop_robot()
print('The Robot has Stopped!')