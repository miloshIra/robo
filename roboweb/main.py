import serial
import time

# WE NEED SOCKETSIO FOR THIS TO WORK <3 !!!!!!!

serial_com = serial.Serial('COM5', 9600)
serial_com.timeout = 1
# asdasdasdasdasdasda#############

def rotate_x_axis(request):
    serial_com.write().endode()


def rotate_y_axis(request):
    pass


def rotate_z_axis(request):
    pass


def move_x_axis_left(request):
    pass


def move_x_axis_right(request):
    pass


def move_y_axis_left(request):
    pass


def move_y_axis_right():
    pass


def move_z_axis_left():
    pass


def move_z_axis_right():
    pass
