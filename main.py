import re
import numpy as nm 
import pytesseract 
import pyautogui
import cv2 
from win10toast import ToastNotifier
from PIL import ImageGrab 
import shelve
import keyboard
import time

data = shelve.open('config')

def main():
    toaster = ToastNotifier()
    

    desired_roll = 82
    pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

    highest = 0

    while True:
        

        cap = ImageGrab.grab(bbox =(data['roll-top'][0], data['roll-top'][1], data['roll-bottom'][0], data['roll-bottom'][1])) 

        greyscale = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)
        out_str = pytesseract.image_to_string(greyscale, lang="eng")

        roll = int(re.search(r"\d+", out_str).group(0).strip())
        print(roll)

        if roll > highest and roll >= desired_roll:
            highest = roll
            toaster.show_toast("Baldur's Gate Rolls",f"Rolled new highest: {roll}, desired was {desired_roll}. Open the BGEE window and RECALL.", threaded=True)
            print(f"Rolled new highest: {roll}, desired was {desired_roll}. Open the BGEE window and RECALL.")
            pyautogui.click(x=data['store'][0], y=data['store'][1])
            
        pyautogui.click(x=data['reroll'][0], y=data['reroll'][1])

keyboard.add_hotkey("ctrl+l", main)