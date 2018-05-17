import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com

def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Driver Assist Remote")
    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

# establishing button controls
    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
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
    root.bind('<u>', lambda event: send_up(mqtt_client))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<j>', lambda event: send_down(mqtt_client))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    self_drive_label = ttk.Label(main_frame, text="Self Drive Mode",background="#ff8533",font=("Helvetica", 16),foreground="#3d3d5c")
    self_drive_label.grid(row=7, column=0)
    self_drive = ttk.Button(main_frame, text="Self drive")
    self_drive.grid(row=8, column=0)
    self_drive['command'] = lambda: follow_line(mqtt_client)
    root.bind('<p>', lambda event: follow_line(mqtt_client))

## gui color
    self_drive_label = ttk.Label(main_frame,text='                        ',font=("Helvetica", 16), background="#ff8533")
    self_drive_label.grid(row=7,column=1)

    self_drive_label = ttk.Label(main_frame, text="Self Drive Mode", font=("Helvetica", 16), background="#ff8533",foreground="#3d3d5c")
    self_drive_label.grid(row=7, column=2)
    self_drive = ttk.Button(main_frame, text="Honk horn")
    self_drive.grid(row=8, column=2)
    self_drive['command'] = lambda: honk(mqtt_client)
    root.bind('<h>', lambda event: honk(mqtt_client))

# establishing video frame
    window = tkinter.Tk()  # Makes main window
    window.wm_title("Rover Camera")
    window.config(background="#006600")
    imageFrame = tkinter.Frame(window, width=600, height=500)
    imageFrame.grid(row=0, column=0, padx=10, pady=2)

#get frames
    lmain = tkinter.Label(imageFrame)
    lmain.grid(row=0, column=0)
    cap = pixy.VideoCapture(0)


    root.mainloop()


def send_up(mqtt_client):
        print("arm_up")
        mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
        print("arm_down")
        mqtt_client.send_message("arm_down")

    # Quit and Exit button callbacks
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
        mqtt_client.send_message("forward_push", [0, 0])


def left(mqtt_client, left_speed_entry, right_speed_entry):
        print('left works')
        mqtt_client.send_message("forward_push", [-int(left_speed_entry.get()), int(right_speed_entry.get())])


def right(mqtt_client, left_speed_entry, right_speed_entry):
        print('Right works')
        mqtt_client.send_message("forward_push", [int(left_speed_entry.get()), -int(right_speed_entry.get())])


def back(mqtt_client, left_speed_entry, right_speed_entry):
        print('back works')
        mqtt_client.send_message("forward_push", [-int(left_speed_entry.get()), -int(right_speed_entry.get())])

def follow_line(mqtt_client):
        print('Stay in lane')
        mqtt_client.send_message("follow_line")

def honk(mqtt_client):
    print('honk honk')
    mqtt_client.send_message("honk")

def show_frame():
    mgtt_client.send_message("show_frame")

main()