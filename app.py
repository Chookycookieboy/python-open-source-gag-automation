import tkinter
from tkinter import *
import time
import keyboard
import threading
import webbrowser

print("""\
      
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     
                                                                                
                                                                                
                    """)

A = True

def stop():
    global A
    A = False

def start():
    global A
    A = True
    time.sleep(5)
    while A == True:
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

def StartThreadFunction(): 
    StartThread = threading.Thread(target=start).start()

def opentut():
    webbrowser.open("https://youtu.be/NZJE5to_AiA")


root = Tk(className="Grow a garden automation")
root.geometry("300x300")
label = Label(root, text='Grow a garden automation V1')

buttonstart = Button(root, text="START automation", command=StartThreadFunction)
buttonstop = Button(root, text="STOP automation", command=stop)

tuttext = Label(root, text='Please watch our tutorial before using!')
tutlabel = Button(root, text='Tutorial', command=opentut)
discord = Label(root, text='add me on discord for update ideas: cookiejeje')


label.pack()
buttonstart.pack()
buttonstop.pack()
tuttext.pack()
tutlabel.pack()
discord.pack()


root.mainloop()