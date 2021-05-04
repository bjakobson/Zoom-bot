# Zoom-bot
<H2>Features</H2>
- Joins Zoom
- Automatically mutes mic and turns off cam
- Leaves Zoom
- Repeats process per class


<H3>Prerequisite:</H3>

- Python verison 3.6 installed
- Zoom installed
- Access to administrative password (Mac & linux sudo)


<h3>Installations:</h3>

1) Mac & Linux:
 - `sudo pip3 install datetime pynput data pyautogui`
2) Windows: 
 - `python -m pip install datetime pynput data pyautogui`
  
<h3>To change data:</h3>
  - Open `data.py` in any editor
  - Follow the template: *URL, Time to join, Time to leave*
  - TIMES MUST BE 24HR TIME
  - Each list is for each day, Monlst - Monday, Tuelst - Tuesday, etc.
  - For windows, open `main.py` in any editor and change line 27, `bjakob` to your username

<h3>To run:</h3>
  - go into your terminal and paste `python3 main.py`
 
Enjoy that extra sleep and let this bot join your Zoom calls for you. This bot will not do anything besides join calls and turn off mic and cam, meaning it will   not be activley taking notes, cannot respond if you are called on, and will not give any reactions or type in chat. Use at your own risk of getting called on.
