# this is Kathi's project
import robot_controller as robo
import ev3dev.ev3 as ev3
import time

import mqtt_remote_method_calls as com




def main():
    robot = robo.Snatch3r

    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()

    pixy = ev3.Sensor(driver_name="pixy-lego")

    pixy.mode = 'SIG1'
    while True:
        print("(X,Y)=({},{}) Width={} Height={}".format(pixy.value(1),pixy.value(2),pixy.value(3),pixy.value(4)))
        time.sleep(1)



# def  find_color(mqtt_client, color_entry):
#
#
#
#
# def what_color(mqtt_client):
main()


