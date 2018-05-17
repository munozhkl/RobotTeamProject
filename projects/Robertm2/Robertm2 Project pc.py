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

    left_speed_label = ttk.Label(main_frame, text='Right Speed')
    left_speed_label.grid()
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.grid(row=1, column=0)

    