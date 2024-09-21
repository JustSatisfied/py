import pyautogui
import time
import random
from analysisGoodsImage import close
from datetime import datetime
from window import activeWindow as window
import getRedis
from trancationInstance import transcation 
from main import main

pyautogui.FAILSAFE = False
last_run_minute = None
transcation_=transcation(False)
window.activate()
 
def sp(st=0,et=1):
    time.sleep(random.uniform(st,et))

def should_run_task(now):
    minute = now.minute
    return (minute==random.randint(15,20)) or (minute==random.randint(30,35))
 

while True:
    now=datetime.now()
    if should_run_task(now) and last_run_minute != now.minute:
        close(transcation_)
        # if transcation_==True:
        #     transcation_.closeActivate()
        last_run_minute = now.minute
        main()
        continue
    else:
     sp(1,3)
     getRedis.getHashHandle()
     main(transcation_)
    
  