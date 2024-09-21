from ocr import ocr
import pyautogui
from mouseMove import move,random_move
import random
import time
from datetime import datetime

now = datetime.now()
minutes = now.minute
def random_sp():
    time.sleep(random.uniform(0.1,0.3))
def analysis(t):
    now = datetime.now()
    minutes = now.minute
    if 0 < minutes < 1:
        y1=470+int(2)*70
        y2=510+int(2)*50
        random_move(1468,y1,1570,y2)
        random_sp()
        pyautogui.click()
        random_sp()
        random_move(1770,1205,1913,1241)
        pyautogui.click()
        random_sp()
        random_move(1207,751,1250,767)
        random_sp()
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        random_sp()
        pyautogui.press('backspace')
        random_sp()
        pyautogui.typewrite(str(random.randint(30,35)), interval=random.uniform(0.2,0.5))
        random_sp()
        random_move(1207,801,1263,819)
        random_sp()
        pyautogui.click()
        random_sp()
        pyautogui.press('backspace',presses=random.randint(5,10),interval=0.1)
        random_sp()
        pyautogui.typewrite(str(135), interval=random.uniform(0.2,0.5))
        random_sp()
        random_move(1065,1139,1187,1176)
        pyautogui.click()
        random_sp()
        random_move(1086,800,1179,834)
        pyautogui.click()
    else:
        result=ocr('./GoodsImage.png')
        goodsValue=[66,110]
        t_flag=False
        for index,value in enumerate(goodsValue):
            try:
                price=int(result[index])
            except ValueError:
                continue
            if value>=price:
                t_flag=True
                y1=470+int(index)*70
                y2=520+int(index)*50
                random_move(1468,y1,1570,y2)
                random_sp()
                pyautogui.click()
                random_sp()
                random_move(1770,1205,1913,1241)
                pyautogui.click()
                random_sp()
                random_move(1207,751,1250,767)
                random_sp()
                pyautogui.doubleClick()
                pyautogui.doubleClick()
                random_sp()
                pyautogui.press('backspace')
                random_sp()
                pyautogui.typewrite(str(random.randint(4,9)), interval=random.uniform(0.2,0.5))
                random_sp()
                random_move(1207,801,1263,819)
                random_sp()
                pyautogui.click()
                random_sp()
                pyautogui.press('backspace',presses=random.randint(5,10),interval=0.1)
                random_sp()
                pyautogui.typewrite(str(value), interval=random.uniform(0.2,0.5))
                random_sp()
                random_move(1065,1100,1187,1139)
                pyautogui.click()
                random_sp()
                random_move(1086,800,1179,834)
                pyautogui.click()
        if(t_flag==False):
            t.addCurrentFlush()
        random_sp()
        random_move(526,1208,562,1238)
        random_sp()
        pyautogui.click()
    

  

def close(t):
    if t.flag==True:
     pyautogui.hotkey('alt', 'y')
     t.close()
     random_sp()
     for i in range(random.randint(2,5)):
      random_move(638,472,1678,1107)
      random_sp()
      pyautogui.click()
