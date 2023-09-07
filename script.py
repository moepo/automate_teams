'''This script joins a meeting at pre-defined time and closes accordingly.'''

import os             
import pyautogui
import time
from time import sleep
from datetime import datetime
import schedule

def joinMeeting():
    os.startfile("link to meeting")
    time.sleep(10)
    mutesound = pyautogui.locateOnScreen("testing.png") 
    print(mutesound)
    pyautogui.moveTo(mutesound)
    pyautogui.click()
    time.sleep(2)
    join = pyautogui.locateOnScreen("join.png") 
    print(join)
    pyautogui.moveTo(join)
    pyautogui.click()
    time.sleep(2)
    
def leaveMeeting():
    check = pyautogui.locateOnScreen("exit.png")
    pyautogui.moveTo(check)
    pyautogui.click()

#schedule for Monday
schedule.every().monday.at("08:02").do(joinMeeting)
schedule.every().monday.at("16:03").do(leaveMeeting)

#schedule for Tuesday
schedule.every().tuesday.at("08:02").do(joinMeeting)
schedule.every().tuesday.at("16:03").do(leaveMeeting)

#schedule for Wednesday
schedule.every().wednesday.at("08:02").do(joinMeeting)
schedule.every().wednesday.at("14:02").do(leaveMeeting)

while True:
    schedule.run_pending()
    time.sleep(2)

