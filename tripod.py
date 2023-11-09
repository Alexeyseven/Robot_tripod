import socket
from tkinter import *
import time
import os
from PIL import Image, ImageTk


s = socket.socket()
s.bind(('192.168.1.241', 2000))
s.listen(1)
os.system('start cmd /k python robot.py')
conn, addr = s.accept()


def send(mes):
    i = 0
    delay = 1/velocity.get()
    while i < value.get():
        conn.send(mes[0])
        time.sleep(delay)
        conn.send(mes[1])
        time.sleep(delay)
        conn.send(mes[2])
        time.sleep(delay)
        i += 1


def up():
    send([b'1', b'3', b'5'])


def down():
    send([b'2', b'4', b'6'])


def left():
    send([b'1', b'4', b'6'])


def right():
    send([b'2', b'3', b'5'])


def close():
    send([b'', b'3', b'6'])


def far():
    send([b'', b'4', b'5'])


def prog_1():
    while True:
        up()

root = Tk()
root.geometry('400x250')

value = IntVar()
velocity = IntVar()

image_up_open = Image.open('up.png')
image_up = ImageTk.PhotoImage(image_up_open)
image_down_open = Image.open('down.png')
image_down = ImageTk.PhotoImage(image_down_open)

image_left_open = Image.open('left.png')
image_left = ImageTk.PhotoImage(image_left_open)
image_right_open = Image.open('right.png')
image_right = ImageTk.PhotoImage(image_right_open)

image_close_open = Image.open('close.png')
image_close = ImageTk.PhotoImage(image_close_open)
image_far_open = Image.open('far.png')
image_far = ImageTk.PhotoImage(image_far_open)

Button(image=image_up, command=up).place(x=107, y=10)
Button(image=image_down, command=down).place(x=107, y=162)
Button(image=image_left, command=left).place(x=15, y=85)
Button(image=image_right, command=right).place(x=200, y=85)
Button(image=image_close, command=close).place(x=15, y=162)
Button(image=image_far, command=far).place(x=200, y=10)
Button(text='prog_1', command=prog_1).place(x=320, y=10)
Entry(textvariable=value, width=7).place(x=127, y=100)
Entry(textvariable=velocity, width=7).place(x=127, y=124)


root.mainloop()