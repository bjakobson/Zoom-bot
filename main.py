#Built by Brandon Jakobson, all rights reserved 5/3/21.


import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import Monlst, Tuelst, Wedlst, Thurlst, Frilst, Testlst
import webbrowser
import pyautogui
import os
from sys import platform
import subprocess

keyboard = Controller()
isStarted = False
list = ""
system = ""
forcekill = ""
print("Application started")



if platform == "darwin":
   system = "open /Applications/zoom.us.app"
   forcekill = "pkill zoom.us"
elif platform == "win32":
   system = r"C:\Users\bjako\AppData\Roaming\Zoom\bin\Zoom.exe"
   forcekill = "taskkill /f /im  Zoom.exe"


os.system(system)
day = datetime.now().strftime("%A")
if day == "Monday":
    list = Monlst
elif day == "Tuesday":
    list = Tuelst
elif day == "Wednesday":
    list = Wedlst
elif day == "Thursday":
    list = Thurlst
elif day == "Friday":
    list = Frilst
print("Using "+day+"'s list")

os.system(forcekill)

for i in list:
    while True:
        if isStarted == False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                os.system(system)
                print("Joined Zoom call")
                webbrowser.open(i[0])
                isStarted = True
        elif isStarted == True:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                print("Left Zoom call")
                os.system(forcekill)
                time.sleep(1)
                isStarted = False
                break

