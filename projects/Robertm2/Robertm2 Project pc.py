import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
mqtt_client = com.MqttClient()
mqtt_client.connect_to_ev3()

def main():
    root = tkinter.Tk()
    root.title('Robot Remote')
    main_frame = ttk.Frame(root, padding='20')
    main_frame.grid()

    right_speed_label = ttk.Label(main_frame, text='Right Speed')
    right_speed_label.grid()
    right_speed_entry = ttk.Entry(main_frame, width=8)
    right_speed_entry.grid(row=1, column= 0)

    left_speed_label = ttk.Label(main_frame, text='Left Speed')
    left_speed_label.grid()
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.grid(row=1, column=1)

    forward_button = ttk.Button(main_frame, text='Forward')
    forward_button.grid()
    forward_button['command'] = lambda: forward(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: forward(mqtt_client, left_speed_entry, right_speed_entry))

    backwards_button = ttk.Button(main_frame, text='Backwards')
    backwards_button.grid()
    backwards_button['command'] = lambda: backwards(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Down>', lambda event: backwards(mqtt_client, left_speed_entry, right_speed_entry))

    right_button = ttk.Button(main_frame, text ='Right')
    right_button.grid()
    right_button['command'] = lambda: right(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Right>', lambda event: right(mqtt_client, left_speed_entry, right_speed_entry))

    left_button = ttk.Button(main_frame, text='Left')
    left_button.grid()
    left_button['command'] = lambda: left(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Left>', lambda event: left(mqtt_client, left_speed_entry, right_speed_entry))

    arm_up_button = ttk.Button(main_frame, text='Arm Up')
    arm_up_button.grid()
    arm_up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<w>', lambda event: send_up(mqtt_client))

    arm_down_button = ttk.Button(main_frame, text='Arm Down')
    arm_down_button.grid()
    arm_down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<s>', lambda event: send_down(mqtt_client))

    stop_button = ttk.Button(main_frame, text='Stop')
    stop_button.grid()
    stop_button['command'] = lambda: stop(mqtt_client)
    root.bind('<space>', lambda event: stop(mqtt_client))


def forward(mqtt_client, left_speed_entry, right_speed_entry):
    print('Forward is working')
    mqtt_client.send_message("forward_push", [int(left_speed_entry.get()), int(right_speed_entry.get())])

def backwards(mqtt_client, left_speed_entry, right_speed_entry):
    print('Backwards is working')
    mqtt_client.send_message("backwards_push", [-int(left_speed_entry.get()), -int(right_speed_entry.get())])

def right(mqtt_client, left_speed_entry, right_speed_entry):
    print('Right is working')
    mqtt_client.send_message("right_push", [int(left_speed_entry()), -int(right_speed_entry())])

def left(mqtt_client, left_speed_entry, right_speed_entry):
    print('Left is working')
    mqtt_client.send_message("left_push", [-int(left_speed_entry()), int(right_speed_entry())])

def send_up(mqtt_client):
    print('Arm up is working')
    mqtt_client.send_message("arm_up")

def send_down(mqtt_client):
    print('Arm down is working')
    mqtt_client.send_message("arm_down")

def stop(mqtt_client):
    print('Stop is working')
    mqtt_client.send_message("forward_push", [0,0])









