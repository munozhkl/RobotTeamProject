# this is Kathi's project
import robot_controller as robo
import ev3dev.ev3 as ev3
import time

import mqtt_remote_method_calls as com

class Teacher(object):
    def __init__(self):
        self.robot = robo.Snatch3r()
        self.pixy = ev3.Sensor(driver_name="pixy_lego")
        print(self.pixy)
        print('made the pixy')

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

    def what_color(self):
        print('Starting what_color')
        self.pixy.mode = 'SIG1'
        width = self.pixy.value(3)
        height = self.pixy.value(4)
        if width*height > 640:
            ev3.Sound.speak('This is the color blue')
        self.pixy.mode = 'SIG2'
        width = self.pixy.value(3)
        height = self.pixy.value(4)
        if width*height > 640:
            ev3.Sound.speak('This is the color green')
        else:
            return "Nothing"

    def see_color(self,signature):
        print('starting see_color')
        self.pixy.mode = signature
        if self.pixy.value(3)*self.pixy.value(4) > 640:
            self.robot.forward_push(0,0)
            return True
            # self.robot.forward_push(0,0)
            # if signature == 'blue':
            #     ev3.Sound.speak('I found the color blue')
            # if signature == 'green':
            #     ev3.Sound.speak('I found the color green')


    def go_find_color(self,signature):
        print('starting go_find_color', signature)
        print(self.pixy)
        time.sleep(1)
        self.pixy.mode = 'SIG1'
        self.robot.forward_push(-300,300)
        # self.see_color()
        # while True:
        #     if self.see_color(signature) is True:
        #         if signature == 'SIG1':
        #             ev3.Sound.speak('I found the color blue')
        #         if signature == 'SIG2':
        #             ev3.Sound.speak('I found the color green')




def main():
    teacher = Teacher()

    mqtt_client = com.MqttClient(teacher)
    mqtt_client.connect_to_pc()


    teacher.loop_forever()

    # pixy = ev3.Sensor(driver_name="pixy-lego")
    #
    # pixy.mode = 'SIG1'
    #
    # while True:
    #     print(pixy.value(1),pixy.value(2),pixy.value(3),pixy.value(4))
    #     time.sleep(1)



# def  find_color(mqtt_client, color_entry):
#
# should I put this in robot controller?
# do I need to use color sensor or camera?
#
# def what_color(mqtt_client):

main()











