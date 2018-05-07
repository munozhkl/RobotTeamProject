"""
Functions for SPINNING the robot LEFT and RIGHT.
Authors: David Fisher, David Mutchler and Kathi Munoz.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implment spin_left_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for spin_left_by_time.
#   Then repeat for spin_left_by_encoders.
#   Then repeat for the spin_right functions.


import ev3dev.ev3 as ev3
import time



def test_spin_left_spin_right():
    """
    Tests the spin_left and spin_right functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets degrees and runs spin_left_by_time.
      3. Same as #2, but runs spin_left_by_encoders.
      4. Same as #1, 2, 3, but tests the spin_right functions.
    """
    # Test spin left seconds:
    seconds = 1
    speed = 0

    while seconds > 0:
        print('Testing Spin Left by Seconds')
        seconds = int(input("Enter seconds to travel: "))
        speed = int(input("Enter speed to travel (from -100 to 100): "))
        stop_action = "brake"
        spin_left_seconds(seconds, speed, stop_action)

    #  Test spin left time

    speed = 0
    degrees = 0
    while -100 <= speed <= 100:
        print('Testing spin left by time')
        speed = int(input("Enter speed to travel (from -100 to 100): "))
        degrees = int(input("Enter degrees to spin: "))
        stop_action = "brake"
        spin_left_by_time(degrees, speed, stop_action)

    # test spin left by encoders

    speed = 0
    degrees = 0
    while -100 <= speed <= 100:
        print('Testing spin left by encoders')
        speed = int(input("Enter speed to travel (from -100 to 100): "))
        degrees = int(input("Enter degrees to spin: "))
        stop_action = "brake"
        spin_left_by_encoders(degrees, speed, stop_action)



    # test spin right by secomds
    seconds = 1
    speed = 0

    while seconds > 0:
        print('Testing spin right by seconds')
        seconds = int(input("Enter seconds to travel: "))
        speed = int(input("Enter speed to travel (from -100 to 100): "))
        stop_action = "brake"
        spin_right_seconds(seconds, speed, stop_action)

    # test spin right by time

    speed = 0
    degrees = 0
    while -100 <= speed <= 100:
        print('Testing spin right by time')
        speed = int(input("Enter speed to travel (from -100 to 100): "))
        degrees = int(input("Enter degrees to spin: "))
        stop_action = "brake"
        spin_right_by_time(degrees, speed, stop_action)

    # test spin right encoders

    speed = 0
    degrees = 0
    while -100 <= speed <= 100:
        print('Testing spin right by encoders')
        speed = int(input("Enter speed to travel (from -100 to 100): "))
        degrees = int(input("Enter degrees to spin: "))
        stop_action = "brake"
        spin_right_by_encoders(degrees, speed, stop_action)


def spin_left_seconds(seconds, speed, stop_action):
    """
    Makes the robot spin in place left for the given number of seconds at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the given stop_action.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp= -speed, stop_action = stop_action)
    right_motor.run_forever(speed_sp = speed, stop_action = stop_action)
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop()



def spin_left_by_time(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    assert left_motor.connected
    assert right_motor.connected

    seconds = degrees / abs(speed)
    left_motor.run_forever(speed_sp = -speed, stop_action = stop_action)
    right_motor.run_forever(speed_sp = speed, stop_action = stop_action)
    time.sleep(seconds)
    left_motor.stop()
    right_motor.stop()




def spin_left_by_encoders(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should spin to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_to_rel_pos(position_sp = -degrees, speed_sp = speed, stop_action = stop_action)
    right_motor.run_to_rel_pos(position_sp = degrees, speed_sp = speed, stop_action = stop_action)
    left_motor.wait_while(ev3.Motor.STATE_RUNNING)
    right_motor.wait_while(ev3.Motor.STATE_RUNNING)
    left_motor.stop()
    right_motor.stop()

def spin_right_seconds(seconds, speed, stop_action):
    """ Calls spin_left_seconds with negative speeds to achieve spin_right motion. """
    spin_left_seconds(seconds, -speed, stop_action)

def spin_right_by_time(degrees, speed, stop_action):
    """ Calls spin_left_by_time with negative speeds to achieve spin_right motion. """
    spin_left_by_time(degrees, -speed, stop_action)

def spin_right_by_encoders(degrees, speed, stop_action):
    """ Calls spin_left_by_encoders with negative speeds to achieve spin_right motion. """
    spin_left_by_encoders(degrees, -speed, stop_action)

test_spin_left_spin_right()