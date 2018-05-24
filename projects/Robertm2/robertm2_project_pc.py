import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com

class MyDelegate(object):
    def print_message(self, message):
        print("Message Received:", message)


def main():
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title('Robot Remote')
    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    right_speed_label = ttk.Label(main_frame, text='Right Speed')
    right_speed_label.grid(row=0, column=0)
    right_speed_entry = ttk.Entry(main_frame, width=8)
    right_speed_entry.grid(row=1, column=0)

    left_speed_label = ttk.Label(main_frame, text='Left Speed')
    left_speed_label.grid(row=0, column=2)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text='Forward')
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: forward(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: forward(mqtt_client, left_speed_entry, right_speed_entry))

    backward_button = ttk.Button(main_frame, text='Backward')
    backward_button.grid(row=4, column=1)
    backward_button['command'] = lambda: backward(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Down>', lambda event: backward(mqtt_client, left_speed_entry, right_speed_entry))

    right_button = ttk.Button(main_frame, text ='Right')
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: right(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Right>', lambda event: right(mqtt_client, left_speed_entry, right_speed_entry))

    left_button = ttk.Button(main_frame, text='Left')
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: left(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Left>', lambda event: left(mqtt_client, left_speed_entry, right_speed_entry))

    arm_up_button = ttk.Button(main_frame, text='Arm Up')
    arm_up_button.grid(row=5, column=0)
    arm_up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<w>', lambda event: send_up(mqtt_client))

    arm_down_button = ttk.Button(main_frame, text='Arm Down')
    arm_down_button.grid(row=6, columm=0)
    arm_down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<s>', lambda event: send_down(mqtt_client))

    stop_button = ttk.Button(main_frame, text='Stop')
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: stop(mqtt_client)
    root.bind('<space>', lambda event: stop(mqtt_client))

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit(mqtt_client, False))

    e_button = ttk.Button(main_frame, text='Exit')
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit(mqtt_client, True))


def forward(mqtt_client, left_speed_entry, right_speed_entry):
    print('Forward is working')
    mqtt_client.send_message("forward_push", [int(left_speed_entry.get()), int(right_speed_entry.get())])

def backward(mqtt_client, left_speed_entry, right_speed_entry):
    print('Backward is working')
    mqtt_client.send_message("forward_push", [-int(left_speed_entry.get()), -int(right_speed_entry.get())])

def right(mqtt_client, left_speed_entry, right_speed_entry):
    print('Right is working')
    mqtt_client.send_message("forward_push", [int(left_speed_entry()), -int(right_speed_entry())])

def left(mqtt_client, left_speed_entry, right_speed_entry):
    print('Left is working')
    mqtt_client.send_message("forward_push", [-int(left_speed_entry()), int(right_speed_entry())])

def send_up(mqtt_client):
    print('Arm up is working')
    mqtt_client.send_message("arm_up")

def send_down(mqtt_client):
    print('Arm down is working')
    mqtt_client.send_message("arm_down")

def stop(mqtt_client):
    print('Stop is working')
    mqtt_client.send_message("forward_push", [0,0])

def quit(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("Shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()

main()







