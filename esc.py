import pyautogui
import time
from mouseMove import move,random_move
import random
import pygetwindow as gw
import TransactionScreenOcr
from analysisGoodsImage import analysis,close
from datetime import datetime

pyautogui.FAILSAFE = False
def find_window_by_title(partial_title):
    for window in gw.getAllWindows():
        if partial_title in window.title:
            return window
    return None
 
 
partial_title = "命运" 
window = find_window_by_title(partial_title)

class transcation:
    def __init__(self,flag):
        self.flag = flag
        self.currentFlush=0
        self.activate=False
    def close(self):
        self.flag=False
    def open(self):
        self.flag=True
    def addCurrentFlush(self):
        print(self.currentFlush)
        if(self.currentFlush==5):
            self.currentFlush=0
            time.sleep(random.randint(120,720))
        else:
            self.currentFlush+=1
    def openActivate(self):
        self.activate=True
    def closeActivate(self):
        self.activate=False
transcation_=transcation(False)

def random_x_y(x1,y1,x2,y2):
    return (random.randint(x1,x2),random.randint(y1,y2))

def ChaoticRandomClick():
    x,y=random_x_y()
    for _ in range(random.randint(2-5)):
        move(x,y)
        pyautogui.click()

 
def sp(st=0,et=1):
    time.sleep(random.uniform(st,et))

def should_run_task(now):
    minute = now.minute
    # 检查当前时间是否在 15-20 分或 30-35 分之间
    return (minute==random.randint(15,20)) or (minute==random.randint(30,35))
def main():  
  if transcation_.activate==False:
       transcation_.openActivate()
       window.activate()
  sp(1,2)
  if transcation_.flag==False:
   pyautogui.hotkey('alt', 'y')
   transcation_.open()
   sp(0,1)
   random_move(550,360,735,391)
   pyautogui.click()
  TransactionScreenOcr.sceen(1452,463,1600,770,"./GoodsImage.png")
  analysis(transcation_)

  
 
window.activate()
last_run_minute = None
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
     sp(3,5)
     main()
    
  