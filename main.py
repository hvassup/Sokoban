#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from time import sleep
import random
from mapper import get_test_path, int_to_str

# Initialize the EV3 Brick.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.D)

robot = DriveBase(left_motor, right_motor, wheel_diameter=43.2, axle_track=114)
DRIVE_SPEED = 100

# Initialize sensors
right_sensor = ColorSensor(Port.S1)
center_sensor = ColorSensor(Port.S2)
left_sensor = ColorSensor(Port.S3)

def drive(turn_rate=0):
    robot.drive(DRIVE_SPEED, turn_rate)

def drive_break():
    for i in range(0, DRIVE_SPEED):
        robot.drive(-DRIVE_SPEED, 0)

def turn(deg):
    if abs(deg) == 180:
        robot.straight(-90)
    else:
        robot.straight(90)
        
    robot.turn(deg)

def ready_for_next_move():
    global current_direction
    current_direction = None
    drive_break()
    print(is_center(), is_right(), is_left())

# Function to adjust for deviations from the grid
def stay_within_the_lines():
    if not is_right() and not is_left():
        drive(0)
    elif is_right() and not is_center() and not is_left():
        drive(35)
    elif not is_right() and not is_center() and is_left():
        drive(-35)
    elif not is_right() and is_center() and is_left():
        ready_for_next_move()
    elif is_right() and is_center() and not is_left():
        ready_for_next_move()
    elif is_right() and is_center() and is_left():
        ready_for_next_move()
    
def is_right():
    return right_sensor.color() == Color.BLACK

def is_center():
    return center_sensor.color() == Color.BLACK

def is_left():
    return left_sensor.color() == Color.BLACK

def push_can():
    print('Push can')
    robot.straight(150)
    robot.straight(-150)

def get_next_move():
    _current_direction, _turn_deg, is_pathway, is_pushing = path.pop(0)
    print('direction:', int_to_str[_current_direction], 'Turn deg', _turn_deg, 'is_pathway', is_pathway, 'is_pushing', is_pushing)
    
    #  or is_pushing and next_turn_deg == 0
    if len(path) > 0:
        next_turn_deg = path[0][1]
    else:
        next_turn_deg = 0
    
    if is_pathway and _turn_deg == 0:
        if not is_pushing or not next_turn_deg:
            print("Discard move")
            continue
    else:
        return _current_direction, _turn_deg, next_turn_deg, is_pushing
    return current_direction, turn_deg, next_turn_deg, is_pushing


# Pop direction
# Turn
# If pathway and 0 degrees turn - skip
# Drive
# When line is hit - current_direction = None
# Repeat
current_direction = None
path = get_test_path()

while True:
    ev3.screen.clear()

    if current_direction == None:
        current_direction, turn_deg, next_turn_deg, is_pushing = get_next_move()
        
        if is_pushing and next_turn_deg != 0 and abs(next_turn_deg) != 180:
            push_can()
            continue
        
        print('Turn',turn_deg)
        turn(turn_deg)
    
    stay_within_the_lines()

    ev3.screen.draw_text(20, 20, 'Right ' + str(is_right()))
    ev3.screen.draw_text(20, 40, 'Center ' + str(is_center()))
    ev3.screen.draw_text(20, 60, 'Left ' + str(is_left()))


# ev3.speaker.play_notes(['C4/12', 'G4/12', 'A4/12', 'C5/8', 'A4/12', 'C5/4'])