import keyboard
import pyautogui
import shelve
import sys
phase = -1

data = shelve.open('config')

def print_controls():
    print("Press CTRL+L to go to the next step.")
    print("Press CTRL+SHIFT+L to go to the previous step.")
    print("Press ESCAPE to exit.")

def forward():
    global phase
    phase += 1
    print_controls()
    print("---------------")
    process_phase()
    print("---------------")
    

def backward():
    global phase
    phase = max(0, phase - 1)
    process_phase()

def process_phase():
    if phase == 0:
        print("Set Baldur's Gate to run in a window. Open OPTIONS->GRAPHICS and uncheck the Full Screen checkbox. Press CTRL+L once you're done.")
    elif phase == 1:
        print("Hover your mouse over the TOP LEFT corner of the Total Roll box. Make sure your mouse is just under the border, on the black background, BUT NOT THE BORDER ITSELF. Press CTRL+L once you're done. Press CTRL+L once it's there.")
    elif phase == 2:
        data["roll-top"] = pyautogui.position()
        print("Hover your mouse over the BOTTOM LEFT corner of the Total Roll box. Make sure your mouse is just above the border, on the black background, BUT NOT THE BORDER ITSELF. Press CTRL+L once you're done. Press CTRL+L once it's there.")    
    elif phase == 3:
        data["roll-bottom"] = pyautogui.position()
        print("Hover your mouse over the REROLL button. Press CTRL+L once it's there.")
    elif phase == 4:
        data["reroll"] = pyautogui.position()
        print("Hover your mouse over the STORE button. Press CTRL+L once it's there.")
    elif phase == 5:
        data["store"] = pyautogui.position()
        print("Press ESCAPE to exit. You can run this anytime again to reconfigure the coords.")    
    elif phase == 6:
        data.close()
        

keyboard.add_hotkey('ctrl+l', forward)
keyboard.add_hotkey('ctrl+shift+l', backward)

forward()

keyboard.wait('esc')