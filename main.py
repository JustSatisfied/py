from config.sceneConfig import ControlNotInSceneList
from Ocr.PaddleOcr import POcr,PictureInfo
import pyautogui
import random 
import time
from work import windowActivate
from mouseMove import random_move
 
pyautogui.FAILSAFE = False
flush_button=[530,1140]
current=0
def sp(st=0,et=1):
    time.sleep(random.uniform(st,et))
    
 

def clickFlushButton():
    global current
    if current<=5:
        current=current+1
    else:
        current=0
        sp(10,15)
    random_move(flush_button[0]+random.uniform(5,15),flush_button[1]+random.uniform(10,15))
    pyautogui.click()
    
def DetermineScene():
    POcr.picture()
    info=PictureInfo.OcrInfo.textMap
   
    for key in ControlNotInSceneList.keys():
         
        action=ControlNotInSceneList[key]["action"]
        validateFc=ControlNotInSceneList[key]["validate"]
        
        if validateFc==False or validateFc(info):
            action()
            break


while True:
    sp(0,1)
    DetermineScene()