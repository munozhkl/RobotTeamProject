"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import math
import time


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    
    def __init__(self):
       self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
       self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
       self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
       self.touch_sensor = ev3.TouchSensor()
       self.color_sensor = ev3.ColorSensor()
       self.ir_sensor = ev3.InfraredSensor()
       self.pixy = ev3.Sensor(driver_name="pixy-lego")

       self.exit = 0

       assert self.left_motor.connected
       assert self.right_motor.connected
       assert self.arm_motor.connected
       assert self.touch_sensor.connected

    def forward(self, inches, speed=100, stop_action='brake'):
        K = 360 / 4.5
        degrees_for_motor = K*inches
        self.left_motor.run_to_rel_pos(speed_sp = 8*speed, position_sp = degrees_for_motor, stop_action = stop_action)
        self.right_motor.run_to_rel_pos(speed_sp=8*speed, position_sp=degrees_for_motor, stop_action=stop_action)
        self.left_motor.wait_while("running")
        self.right_motor.wait_while("running")


    def backward(self, inches, speed=100, stop_action='brake'):
        K = 360 / 4.5
        degrees_for_motor = K*inches
        self.left_motor.run_to_rel_pos(speed_sp = -8*speed, position_sp = degrees_for_motor, stop_action = stop_action)
        self.right_motor.run_to_rel_pos(speed_sp=-8*speed, position_sp=degrees_for_motor, stop_action=stop_action)
        self.left_motor.wait_while("running")
        self.right_motor.wait_while("running")


    def spin_left(self, degrees, speed,stop_action='brake'):

        self.left_motor.run_to_rel_pos(position_sp=-degrees, speed_sp=speed, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=degrees, speed_sp=speed, stop_action=stop_action)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.stop()
        self.right_motor.stop()


    def spin_right(self, degrees, speed, stop_action = 'brake'):

        self.left_motor.run_to_rel_pos(position_sp=-degrees, speed_sp=-speed, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=degrees, speed_sp=-speed, stop_action=stop_action)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.stop()
        self.right_motor.stop()

    def turn_left(self, degrees, speed, stop_action = 'brake'):
        self.left_motor.run_to_rel_pos(speed_sp=-speed, position_sp=degrees, stop_action=stop_action)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.stop()

    def turn_right(self, degrees, speed, stop_action= 'brake'):
        self.left_motor.run_to_rel_pos(speed_sp=speed, position_sp=degrees, stop_action=stop_action)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.stop()

    def forward_push(self,left_speed,right_speed):
        self.right_motor.run_forever(speed_sp=right_speed)
        self.left_motor.run_forever(speed_sp=left_speed)

    def shutdown(self):
        self.right_motor.run_forever(speed_sp=0)
        self.left_motor.run_forever(speed_sp=0)
        self.exit = 1

    def arm_calibration(self):
        self.arm_motor.run_forever(speed_sp=900)
        while True:
            if self.touch_sensor.is_pressed == False:
                time.sleep(0.01)
            else:
                break
        self.arm_motor.stop(stop_action="brake")
        ev3.Sound.beep().wait()

        arm_revolutions_for_full_range = 14.2 * 360
        self.arm_motor.run_to_rel_pos(position_sp=-arm_revolutions_for_full_range)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)

        self.arm_motor.position = 0

    def arm_up(self):
        self.arm_motor.run_forever(speed_sp=900)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action="brake")
        ev3.Sound.beep()

    def arm_down(self):
        self.arm_motor.run_to_abs_pos(position_sp=0)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)  # Blocks until the motor finishes running
        ev3.Sound.beep()

    def loop_forever(self):
        while True:
            if self.exit == 1:
                break
            time.sleep(.05)

    def honk(self):
        ev3.Sound.beep().wait()
        ev3.Sound.speak('get out of my way').wait()

    def follow_line(self):
        while True:
            if self.color_sensor.reflected_light_intensity <= 80:
                self.right_motor.run_forever(speed_sp=300)
                self.left_motor.run_forever(speed_sp=100)

            if self.color_sensor.reflected_light_intensity > 80:
                self.left_motor.run_forever(speed_sp=300)
                self.right_motor.run_forever(speed_sp=100)

            if self.ir_sensor.proximity <= 10:
                break
        self.left_motor.run_forever(speed_sp=0)
        self.right_motor.run_forever(speed_sp=0)
        ev3.Sound.speak('uh oh').wait()


##### video camera
    def show_frame(self):
        while True:
            self.pixy



