# this is the pc file

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
#  make the pc delegate... but what exactly would the pc receive from the robot?


class DelegateForPC(object):

    def color_found(self,color_string):
        print('The robot has found the color', color_string)
        self.color['text'] = color_string






def main():
    pc_delegate = DelegateForPC()
    mqtt_client = com.MqttClient(pc_delegate)
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title('Robot Remote')
    main_frame = ttk.Frame(root, padding= 20)
    main_frame.grid()

    color_entry_button = ttk.Button(main_frame,text='Find the color:')
    color_entry_button.grid(row=1,column=3)
    color_entry = ttk.Entry(main_frame,width=8)
    color_entry.grid(row=2,column=3)
    color_entry_button['command'] = lambda: find_color(mqtt_client,color_entry.get())
    color_found_label = ttk.Label(main_frame,text='Color Found:')
    color_found_label.grid(row=1, column=4)
    color = ttk.Label(main_frame,text='???')
    color.grid(row=2,column=4)
    pc_delegate.color = color

    what_color_btn = ttk.Button(main_frame,text='What color is this?')
    what_color_btn.grid(row=3, column=3)
    what_color_btn['command'] = lambda: what_color(mqtt_client)

    left_speed_label = ttk.Label(main_frame, text="Left Speed")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right Speed")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: forward(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: forward(mqtt_client, left_speed_entry, right_speed_entry))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    # left_button and '<Left>' key
    left_button['command'] = lambda: left(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Left>', lambda event: left(mqtt_client, left_speed_entry, right_speed_entry))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    # stop_button and '<space>' key (note, does not need left_speed_entry, right_speed_entry)
    stop_button['command'] = lambda: stop(mqtt_client)
    root.bind('<space>', lambda event: stop(mqtt_client))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    # right_button and '<Right>' key
    right_button['command'] = lambda: right(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Right>', lambda event: right(mqtt_client, left_speed_entry, right_speed_entry))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    # back_button and '<Down>' key
    back_button['command'] = lambda: back(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Down>', lambda event: back(mqtt_client, left_speed_entry, right_speed_entry))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)


    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)


    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


#goes and finds the color entered, need to make function in robot
def find_color(mqtt_client,color_entry):
    print('Finding the color', color_entry )
    if color_entry == 'blue':
        mqtt_client.send_message('go_find_color', ['SIG1'])
    if color_entry == 'green':
        mqtt_client.send_message('go_find_color', ['SIG2'])



def what_color(mqtt_client):
    # maybe the pc could recieve the color in text form as well
    print('what color is this?')
    mqtt_client.send_message('what_color')


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()

def forward(mqtt_client, left_speed_entry, right_speed_entry):
    print('forward works')
    mqtt_client.send_message("forward_push", [int(left_speed_entry.get()), int(right_speed_entry.get())])


def stop(mqtt_client):
    print('stop works')
    mqtt_client.send_message("forward_push", [0,0])


def left(mqtt_client, left_speed_entry, right_speed_entry):
    print('left works')
    mqtt_client.send_message("forward_push", [-int(left_speed_entry.get()),int(right_speed_entry.get()) ])


def right(mqtt_client, left_speed_entry, right_speed_entry):
    print('Right works')
    mqtt_client.send_message("forward_push", [int(left_speed_entry.get()), -int(right_speed_entry.get())])


def back(mqtt_client, left_speed_entry, right_speed_entry):
    print('back works')
    mqtt_client.send_message("forward_push", [-int(left_speed_entry.get()), -int(right_speed_entry.get())])


def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")



main()







