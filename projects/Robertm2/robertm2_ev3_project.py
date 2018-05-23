#
import robot_controller as robo
import ev3dev.ev3 as ev3
import mqtt_remote_method_calls as com

class Trainer(object):
    def __init__(self, pixy):
        self.robot = robo.Snatch3r()
        self.pixy = pixy

    def loop_forever(self):
        self.robot.loop_forever()

    def forward_push(self, left_speed_entry, right_speed_entry):
        self.robot.forward_push(left_speed_entry, right_speed_entry)

    def backward_push(self, left_speed_entry, right_speed_entry):
        self.robot.backward_push(left_speed_entry, right_speed_entry)

    def arm_up(self):
        self.robot.arm_up()

    def arm_down(self):
        self.robot.arm_down()

    def shutdown(self):
        self.robot.shutdown()




