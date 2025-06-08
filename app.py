import tkinter
from tkinter import *
import time
import keyboard


def start():
    time.sleep(3)
    while True:
        for i in range (7):
            time.sleep(0.1)
            keyboard.press_and_release("enter")
            time.sleep(0.1)
            keyboard.press_and_release("s")
            time.sleep(0.1)
            keyboard.press_and_release("enter")
            time.sleep(0.1)
            keyboard.press_and_release("enter")
            time.sleep(0.1)
            keyboard.press_and_release("enter")
            time.sleep(0.1)
            keyboard.press_and_release("w")
            time.sleep(0.1)
            keyboard.press_and_release("w")
        for i in range(8):
            time.sleep(0.1)
            keyboard.press_and_release("s")

root = Tk(className="Grow a garden automation")
root.geometry("300x300")
label = Label(root, text='Grow a garden automation V1')

button = Button(root, text="Start automation", command=start)

tuttext = Label(root, text='Please watch our tutorial before using!')
tutlabel = Label(root, text='link')
discord = Label(root, text='add me on discord for update ideas: cookiejeje')

label.pack()
button.pack()
tuttext.pack()
tutlabel.pack()
discord.pack()


root.mainloop()
