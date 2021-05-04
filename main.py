#Built by Brandon Jakobson, all rights reserved 5/3/21.


import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import Monlst, Tuelst, Wedlst, Thurlst, Frilst
import webbrowser
import pyautogui
import os

keyboard = Controller()
isStarted = False
list = ""
print("Application started")
 

    
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

os.system("open /Applications/zoom.us.app")
for i in list:
    while True:
        if isStarted == False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                os.system("open /Applications/zoom.us.app")
                print("Joined Zoom call")
                webbrowser.open(i[0])
                isStarted = True
        elif isStarted == True:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                print("logging out")
                os.system("pkill zoom.us")
                time.sleep(1)
                isStarted = False
                break
