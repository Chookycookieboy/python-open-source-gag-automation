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
    class AlwaysTrue:
        def get(self): return True

    fruits = [
        (AlwaysTrue(), "Ember Lily"),
        (Beanstalk, "Beanstalk"),
        (Cacao, "Cacao"),
        (Pepper, "Pepper"),
        (Mushroom, "Mushroom"),
        (Grape, "Grape"),
        (Mango, "Mango"),
        (Dragon, "Dragon"),
        (Cactus, "Cactus"),
        (Coconut, "Coconut"),
        (Bamboo, "Bamboo"),
        (Apple, "Apple"),
        (Pumpkin, "Pumpkin"),
        (Watermelon, "Watermelon"),
    ]

    global A
    A = True
    time.sleep(2)

    while A:
        selected_indices = [i for i, (var, _) in enumerate(fruits) if var.get()]
        if not selected_indices:
            time.sleep(0.5)
            continue

        current_idx = 0 
        for target_idx in selected_indices:
            steps = target_idx - current_idx
            for _ in range(steps):
                keyboard.press_and_release("w")
                time.sleep(0.1)
            current_idx = target_idx
            # Buy the fruit
            keyboard.press_and_release("enter")
            time.sleep(0.1)
            keyboard.press_and_release("s")
            for i in range(5):
                keyboard.press_and_release("enter")
                time.sleep(0.2)
            keyboard.press_and_release("w")

        for _ in range(current_idx):
            keyboard.press_and_release("s")
            time.sleep(0.1)
        time.sleep(0.5)

def StartThreadFunction(): 
    StartThread = threading.Thread(target=start).start()

def opentut():
    webbrowser.open("https://youtu.be/NZJE5to_AiA")


root = Tk(className="Grow a garden automation")
root.geometry("300x500")
label = Label(root, text='Grow a garden automation V1')

Beanstalk = BooleanVar()
Cacao = BooleanVar()
Pepper = BooleanVar()
Mushroom = BooleanVar()
Grape = BooleanVar()
Mango = BooleanVar()
Dragon = BooleanVar()
Cactus = BooleanVar()
Coconut = BooleanVar()
Bamboo = BooleanVar()
Apple = BooleanVar()
Pumpkin = BooleanVar()
Watermelon = BooleanVar()

checkmark1 = Checkbutton(root, text="Beanstalk", variable=Beanstalk)
checkmark2 = Checkbutton(root, text="Cacao", variable=Cacao)
checkmark3 = Checkbutton(root, text="Pepper", variable=Pepper)
checkmark4 = Checkbutton(root, text="Mushroom", variable=Mushroom)
checkmark5 = Checkbutton(root, text="Grape", variable=Grape)
checkmark6 = Checkbutton(root, text="Mango", variable=Mango)
checkmark7 = Checkbutton(root, text="Dragon", variable=Dragon)
checkmark8 = Checkbutton(root, text="Cactus", variable=Cactus)
checkmark9 = Checkbutton(root, text="Coconut", variable=Coconut)
checkmark10 = Checkbutton(root, text="Bamboo", variable=Bamboo)
checkmark11 = Checkbutton(root, text="Apple", variable=Apple)
checkmark12 = Checkbutton(root, text="Pumpkin", variable=Pumpkin)
checkmark13 = Checkbutton(root, text="Watermelon", variable=Watermelon)

buttonstart = Button(root, text="START automation", command=StartThreadFunction)
buttonstop = Button(root, text="STOP automation", command=stop)

tuttext = Label(root, text='Please watch our tutorial before using!')
tutlabel = Button(root, text='Tutorial', command=opentut)
discord = Label(root, text='add me on discord for update ideas: cookiejeje')


label.pack()
buttonstart.pack()
buttonstop.pack()
tuttext.pack()

checkmark1.pack()
checkmark2.pack()
checkmark3.pack()
checkmark4.pack()
checkmark5.pack()
checkmark6.pack()
checkmark7.pack()
checkmark8.pack()
checkmark9.pack()
checkmark10.pack()
checkmark11.pack()
checkmark12.pack()
checkmark13.pack()

tutlabel.pack()
discord.pack()



root.mainloop()