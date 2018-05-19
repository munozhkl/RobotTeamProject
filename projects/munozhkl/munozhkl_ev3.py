# this is Kathi's project
import robot_controller as robo
import ev3dev.ev3 as ev3
import time

import mqtt_remote_method_calls as com

class Teacher(object):
    def __init__(self, pixy):
        self.robot = robo.Snatch3r()
        self.pixy = pixy
        print(pixy.value(1))
        print(self.pixy.value(1))
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
        print(self.pixy.mode)
        self.pixy.mode = 'SIG1'
        print(self.pixy.mode)
        time.sleep(0.5)
        width = self.pixy.value(3)
        height = self.pixy.value(4)
        if width*height > 50:
            ev3.Sound.speak('This is the color blue').wait()
            ev3.Sound.speak('B, L, U, E').wait()

        self.pixy.mode = 'SIG2'
        print(self.pixy.mode)
        time.sleep(0.5)
        width = self.pixy.value(3)
        height = self.pixy.value(4)
        if width*height > 50:
            ev3.Sound.speak('This is the color green').wait()
            ev3.Sound.speak('G, R, E, E, N').wait()
        else:
            ev3.Sound.speak('I do not see anything')

    def see_color(self,signature):
        print('starting see_color')
        self.pixy.mode = signature
        if self.pixy.value(3)*self.pixy.value(4) > 100:
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
        self.pixy.mode = signature
        print(self.pixy.mode)
        time.sleep(1)
        # print(self.pixy.value(1))
        # time.sleep(1)
        self.robot.forward_push(-300,300)

        while True:
            if self.see_color(signature) is True:
                if signature == 'SIG1':
                    ev3.Sound.speak('I found the color blue').wait()
                    ev3.Sound.speak('Spell the word blue').wait()
                    ev3.Sound.speak('B, L, U, E').wait()
                    break
                if signature == 'SIG2':
                    ev3.Sound.speak('I found the color green').wait()
                    ev3.Sound.speak('Spell the word green').wait()
                    ev3.Sound.speak('G, R, E, E, N').wait()
                    break




def main():
    pixy = ev3.Sensor(driver_name="pixy-lego")
    print(pixy.value(1))
    teacher = Teacher(pixy)

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











