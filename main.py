import pyautogui
import time
from mouseMove import move,random_move
import random
import TransactionScreenOcr
from analysisGoodsImage import analysis,close
from window import activeWindow as window

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
    return (minute==random.randint(15,20)) or (minute==random.randint(30,35))
def main(transcation_):  
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
