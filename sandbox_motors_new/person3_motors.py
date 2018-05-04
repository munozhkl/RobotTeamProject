"""
Functions for TURNING the robot LEFT and RIGHT.
Authors: David Fisher, David Mutchler and Madison Robertson
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implment turn_left_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for turn_left_by_time.
#   Then repeat for turn_left_by_encoders.
#   Then repeat for the turn_right functions.

import ev3dev.ev3 as ev3
import time


def test_turn_left_turn_right():
    """
    Tests the turn_left and turn_right functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets degrees and runs turn_left_by_time.
      3. Same as #2, but runs turn_left_by_encoders.
      4. Same as #1, 2, 3, but tests the turn_right functions.

    """

    seconds = 1
    while seconds != 0:
        seconds = int(input("Enter a time to drive (in seconds):"))
        speed = (int(input("Enter an integer for the left motor (between -100 to 100):")))*8
        stop_action = "brake"
        turn_left_seconds(seconds, speed, stop_action)


    speed = 0
    while -100 <= speed <= 100:
        speed = (int(input("Enter an integer for speed:"))*8)
        degrees = (int(input("Enter an integer for degrees:")))
        stop_action = "brake"
        turn_left_by_time(degrees, speed, stop_action)


    seconds = 1
    while seconds != 0:
        seconds = (int(input("Enter a time to drive (in seconds):")))
        speed = (int(input("Enter an integer for the right motor (between -100 to 100):"))*8)
        stop_action = "brake"
        turn_right_seconds(seconds, speed, stop_action)



def turn_left_seconds(seconds, speed, stop_action):
    """
    Makes the robot turn in place left for the given number of seconds at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the given stop_action.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    assert left_motor.connected
    left_motor.run_forever(speed_sp= -speed,stop_action = stop_action)
    time.sleep(seconds)
    left_motor.stop()



def turn_left_by_time(degrees, speed, stop_action):
    """
    Makes the robot turn in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    assert left_motor.connected
    left_motor.run_forever(speed_sp=-speed, stop_action=stop_action)
    seconds = abs(degrees*9.555 / speed*8)
    time.sleep(seconds)
    left_motor.stop()


def turn_left_by_encoders(degrees, speed, stop_action):
    """
    Makes the robot turn in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should turn to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """


def turn_right_seconds(seconds, speed, stop_action):
    """ Calls turn_left_seconds with negative speeds to achieve turn_right motion. """
    turn_left_seconds(seconds, -speed, stop_action)


def turn_right_by_time(degrees, speed, stop_action):
    """ Calls turn_left_by_time with negative speeds to achieve turn_right motion. """
    turn_left_by_time(degrees, -speed, stop_action)



def turn_right_by_encoders(degrees, speed, stop_action):
    """ Calls turn_left_by_encoders with negative speeds to achieve turn_right motion. """
    turn_left_by_encoders(degrees, -speed, stop_action)


test_turn_left_turn_right()