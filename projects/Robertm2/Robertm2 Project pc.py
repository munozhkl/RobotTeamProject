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
    backwards_entry = ttk.Entry(main_frame, width=8)
    backwards_entry.grid(row= 2, column=1)

def forward(mqtt_client, left_speed_entry, right_speed_entry):
    print('Forward is working')
    mqtt_client.send_message("forward_push", [int(left_speed_entry.get()), int(right_speed_entry.get())])








