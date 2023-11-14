import socket
from tkinter import *
import time
import os
from PIL import Image, ImageTk
import keyboard


s = socket.socket()
s.bind(('192.168.1.241', 2000))
s.listen(4)
os.system('start cmd /k python robot.py')
conn, addr = s.accept()

stack = []


def run():
    while not keyboard.is_pressed('q'):
        for i in stack:
            print(stack)
            conn.send(i)
            print(conn.recv(50))


def up():
    global stack
    stack.append(str.encode('u' + str(value_up.get())))


def down():
    global stack
    stack.append(str.encode('d' + str(value_down.get())))


def right():
    global stack
    stack.append(str.encode('r' + str(value_right.get())))


def left():
    global stack
    stack.append(str.encode('l' + str(value_left.get())))


def close():
    global stack
    stack.append(str.encode('c' + str(value_close.get())))


def far():
    global stack
    stack.append(str.encode('f' + str(value_far.get())))


def prog():
    Label(root, text=stack).place(x=200, y=140)


def clr():
    global stack
    stack = []    


root = Tk()
root.geometry('400x437')

value_up = IntVar()
value_down = IntVar()
value_right = IntVar()
value_left = IntVar()
value_close = IntVar()
value_far = IntVar()

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

image_run_open = Image.open('run.png')
image_run = ImageTk.PhotoImage(image_run_open)

Button(image=image_run, text='RUN', command=run).place(x=270, y=10)
Button(text='PROG', command=prog).place(x=270, y=100)
Button(text='CLR', command=clr).place(x=270, y=170)
Button(image=image_up, command=up).place(x=10, y=10)
Button(image=image_down, command=down).place(x=10, y=80)
Button(image=image_right, command=right).place(x=10, y=150)
Button(image=image_left, command=left).place(x=10, y=220)
Button(image=image_close, command=close).place(x=10, y=290)
Button(image=image_far, command=far).place(x=10, y=360)
Entry(textvariable=value_up, width=7).place(x=100, y=40)
Entry(textvariable=value_down, width=7).place(x=100, y=110)
Entry(textvariable=value_right, width=7).place(x=100, y=180)
Entry(textvariable=value_left, width=7).place(x=100, y=260)
Entry(textvariable=value_close, width=7).place(x=100, y=330)
Entry(textvariable=value_far, width=7).place(x=100, y=400)


while True:
    if keyboard.is_pressed('esc'):
        break    
    root.update()