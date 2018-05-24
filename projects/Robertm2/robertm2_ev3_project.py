#
import robot_controller as robo
import ev3dev.ev3 as ev3
import mqtt_remote_method_calls as com

class Trainer(object):
    def __init__(self, pixy):
        self.robot = robo.Snatch3r()
        self.pixy = pixy
        self.mqtt_client = None

    def loop_forever(self):
        self.robot.loop_forever()

    def forward_push(self, left_speed_entry, right_speed_entry):
        self.robot.forward_push(left_speed_entry, right_speed_entry)

    def arm_up(self):
        self.robot.arm_up()

    def arm_down(self):
        self.robot.arm_down()

    def shutdown(self):
        self.robot.shutdown()

    def spots_pokemon(self):
        self.pixy.mode = 'SIG1'
        width = self.pixy.value(3)
        height = self.pixy.value(4)
        if width*height > 100:
            ev3.Sound.speak('I caught Bulbasaur').wait()
        self.pixy.mode = 'SIG2'
        width = self.pixy.value(3)
        height = self.pixy.value(4)
        if width*height > 100:
            ev3.Sound.speak('I caught Squritle ').wait()
        self.pixy.mode = 'SIG3'
        width = self.pixy.value(3)
        height = self.pixy.value(4)
        if width*height > 100:
            ev3.Sound.speak('I caught Charmander').wait()


def main():
    pixy = ev3.Sensor(driver_name = "pixy-lego")
    trainer = Trainer(pixy)
    mqtt_client = com.MqttClient(trainer)
    trainer.mqtt_client = mqtt_client
    mqtt_client.connect_to_pc()

    trainer.loop_forever()

main()
