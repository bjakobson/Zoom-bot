# Zoom-bot
<H2>Features</H2>
 1) Joins Zoom<br>
 2) Automatically mutes mic and turns off cam<br>
 3) Leaves Zoom<br>
 4) Repeats process per class<br>


<H3>Prerequisite:</H3>
- Download or clone this repository
- Python verison 3.6 installed
- Zoom installed
- Access to administrative password (Mac & linux sudo)


<h3>Installations:</h3>

1) Mac & Linux:
 - `sudo pip3 install datetime pynput data pyautogui`
2) Windows: 
 - `python -m pip install datetime pynput data pyautogui`
  
<h3>To change data:</h3>
  - Open `data.py` in any editor<br>
  - Follow the template: *URL, Time to join, Time to leave*<br>
  - TIMES MUST BE 24HR TIME<br>
  - Each list is for each day, Monlst - Monday, Tuelst - Tuesday, etc.<br>
  - For windows, open `main.py` in any editor and change line 27, `bjakob` to your username<br>

<h3>To run:</h3>
  - go into your terminal and type `python3 main.py`


<br><br>
Enjoy that extra sleep and let this bot join your Zoom calls for you. This bot will not do anything besides join calls and turn off mic and cam, meaning it will   not be activley taking notes, cannot respond if you are called on, and will not give any reactions or type in chat. Use at your own risk of getting called on.
