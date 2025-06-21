 
import pyautogui
from mouseMove import move,random_move
import random
import time
from datetime import datetime
from PaddleOcr import Ocr
import TransactionScreenOcr
from work import windowActivate
 
 
 
def sp(st=0,et=1):
    time.sleep(random.uniform(st,et))
    
now = datetime.now()

minutes = now.minute

screen_x=322 
screen_y=250
screen_x1=1931
screen_y1=1249

commodity_price={
    "裁缝术：梦幻[16-19]":23,
    "衰落":90,
    "庇护":220,
    "金术":45,
   
}

 
commodity_name=[]

default_commodity_price=1050

array=[]

flush_button=[530,1205]
continuousOperationStep=0

def fuzzy_match_commodity_name():
    global commodity_name
    for key in commodity_price:
        commodity_name.append(key)
fuzzy_match_commodity_name()

def clickFlushButton():
    random_move(flush_button[0]+random.uniform(5,15),flush_button[1]+random.uniform(10,15))
    pyautogui.click()
    
def isOpenTransaction(posResult,titleResult):
    for titleIndex,titleValue in enumerate(titleResult):
        if "物品交易所" in titleValue:
            return False 
    pyautogui.hotkey("alt","y")
    sp(1,3)
    TransactionScreenOcr.sceen(screen_x,screen_y,screen_x1,screen_y1,"./result.png")
    bbox,text,confidence=Ocr("result.png")
    print(text)
    clickMyButton(bbox,text)
def clickMyButton(posResult,titleResult):
      for titleIndex,titleValue in enumerate(titleResult):
        print(titleValue)
        if "关注" in titleValue:
            x=posResult[titleIndex][0][0]+random.uniform(50,60)+screen_x
            y=posResult[titleIndex][0][1]+random.uniform(5,10)+screen_y
            print("存在关注目录",x,y)
            random_move(x,y)
            pyautogui.click()
def priceTooHigh(posResult,titleResult):
  pyautogui.hotkey('esc', 'esc') 
    
def currentItemFuzzyMatch(target_string):
    flag=False
    for item in commodity_name:
     if item in target_string:
        flag=True
    return flag

def getCommodityPrice(posResult,titleResult,CertaintyResult,index):
    distance_array=[]
    for i in range(3):
        indexResult=i+1
        if CertaintyResult[index+indexResult]>0.8 and currentItemFuzzyMatch(titleResult[index+indexResult])!=True:
          distance_array.append([posResult[index+indexResult][0][0],posResult[index+indexResult][0][1],i,titleResult[index+indexResult]])
        else:
           return []
    if len(distance_array)<3:
        return []
    for i in range(len(distance_array) - 1):
        if distance_array[i+1][2] != distance_array[i][2] + 1:
          return []
    return distance_array[len(distance_array)-1]

def exitBuyMouseMoveTo(posResult,titleResult):
    global array
    for titleIndex,titleValue in enumerate(titleResult):
        if titleValue=="购买数量":
            x=posResult[titleIndex][0][0]+random.uniform(250,300)+screen_x
            y=posResult[titleIndex][0][1]+random.uniform(5,10)+screen_y
            random_move(x,y)
            sp()
            pyautogui.click()
            pyautogui.doubleClick()
            pyautogui.doubleClick()
            sp()
            pyautogui.press('backspace')
            pyautogui.typewrite(str(random.randint(10,15)), interval=random.uniform(0.2,0.5))
            
        if "近似值" in titleValue:
            x=posResult[titleIndex][0][0]+random.uniform(250,300)+screen_x
            y=posResult[titleIndex][0][1]+random.uniform(5,10)+screen_y
            random_move(x,y)
            sp()
            pyautogui.click()
            sp()
            pyautogui.press('backspace',presses=random.randint(5,10),interval=0.1)
            sp()
                     
            pyautogui.typewrite(str(commodity_price[array[5]]), interval=random.uniform(0.2,0.5))

        if "购买"==titleValue:
            x=posResult[titleIndex][0][0]+random.uniform(50,60)+screen_x
            y=posResult[titleIndex][0][1]+random.uniform(5,10)+screen_y
            random_move(x,y)
            sp()
            pyautogui.click()
            return 
    
def analysisOcrResult(titleResult,posResult,CertaintyResult):
    global array
    buyButtonPos=[]
    current_commodity_price={}
    for index,title in enumerate(commodity_name):
        current_commodity_price[title]=False;
    for titleIndex,titleValue in enumerate(titleResult):
        if "购买" in titleValue:
            buyButtonPos=posResult[titleIndex][0]
        if currentItemFuzzyMatch(titleValue):
           array=getCommodityPrice(posResult,titleResult,CertaintyResult,titleIndex)
           if len(array)!=0:
               for key in commodity_price:
                   if key in titleValue:
                      current_commodity_price[key]=array
     
    for commodity in commodity_name:
        current=current_commodity_price[commodity]
        try:
            if current!=False and commodity_price[commodity]>int(current[3]):
                array=current_commodity_price[commodity]
                array.append(buyButtonPos)
                array.append(commodity)
              
                return array
        except ValueError as e:
                return []

def transactionPage( bbox,text,confidence):
    global continuousOperationStep
    array=analysisOcrResult(text,bbox,confidence)
  
    if array==None:
       clickFlushButton()
       continuousOperationStep=continuousOperationStep+1
    if isinstance(array,list) and len(array):
        random_move(array[0]+random.uniform(100,150)+screen_x,array[1]+random.uniform(10,20)+screen_y)
        pyautogui.click()
        random_move(int(array[4][0])+random.uniform(30,50)+screen_x,int(array[4][1])+random.uniform(10,20)+screen_y)
        pyautogui.click()
        continuousOperationStep=0
        
def successTransaction(bbox,text):
       for titleIndex,titleValue in enumerate(text):
           if "确认" == titleValue:
            x=bbox[titleIndex][0][0]+random.uniform(40,50)+screen_x
            y=bbox[titleIndex][0][1]+random.uniform(5,10)+screen_y
            random_move(x,y)
            sp()
            pyautogui.click()
    
def judgeCurrentStep( bbox,text,confidence):
    isOpenTransaction(bbox,text)
    
    for titleIndex,titleValue in enumerate(text):
         if "警告" in titleValue:     
            return priceTooHigh(bbox,text)    
    for titleIndex,titleValue in enumerate(text):
            
        if "购买数量" in titleValue:
            return exitBuyMouseMoveTo( bbox,text)
        if "购买成功" in titleValue:
            return successTransaction(bbox,text)
        
    clickFlushButton()
    return transactionPage( bbox,text,confidence)

 
def main():
    global continuousOperationStep
    while True:
     try:
        time.sleep(0.5)
        if continuousOperationStep == 5:
            time.sleep(random.uniform(10,15))
            continuousOperationStep=0
        TransactionScreenOcr.sceen(screen_x,screen_y,screen_x1,screen_y1,"./result.png")
        bbox,text,confidence=Ocr("result.png")
        time.sleep(0.5)
        judgeCurrentStep(bbox,text,confidence)
     except IndexError as e:
         continue
     except ValueError as e:
         continue
main()       
        
