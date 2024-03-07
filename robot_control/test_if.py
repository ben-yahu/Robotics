from robot_control_class import RobotControl

rc = RobotControl()

wall_Dist = rc.get_laser(360)

if wall_Dist < 1:
    rc.stop_robot()
else:
    rc.move_straight()

print('Wall distance:', wall_Dist)
