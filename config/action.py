from .price  import commodity_price
from Ocr.PaddleOcr import POcr,PictureInfo
from .controll import ControlList
from .globalVariable import currentAllowBuyTrascation,currentTrascationPageOpen
from mouseMove import move,random_move
import pyautogui
import time
import random
from Ocr.screen import offset_x,offset_y

flush_button=[530,1213]

def clickFlushButton():
    random_move(flush_button[0]+random.uniform(5,15),flush_button[1]+random.uniform(10,15))
    pyautogui.click()
    
    
def sp(st=0,et=1):
    time.sleep(random.uniform(st,et))

def is_number(s):
    try:
        float(s)  # 尝试将字符串转换为浮点数
        return True
    except ValueError:
        # 如果转换失败，说明不是有效的数字字符串
        return False
def PurchaseGoodsSuccessAction():
    successBuyButtonMeta=ControlList['successBuyButton']
    successBuyButtonPosition=None
    if successBuyButtonMeta["init"]==True:
       successBuyButtonPosition=successBuyButtonMeta["position"]
    if successBuyButtonMeta["init"]==False and successBuyButtonMeta["allowCache"]==True:
        successBuyButtonPosition=PictureInfo.OcrInfo.getKeyOfPosition("确认",30,5)
        successBuyButtonMeta["position"]=successBuyButtonPosition
        successBuyButtonMeta["init"]=True
    else:
        random_move(successBuyButtonPosition[0],successBuyButtonPosition[1])
        pyautogui.click()

def PurchaseGoodsActions():
    
    global currentAllowBuyTrascation
    buyQuantityMeta=ControlList["buyQuantity"]
    averageMeta=ControlList["average"]
    buyQuantitySuccessButtonMeta=ControlList["buyQuantitySuccessButton"]
    successBuyButtonMeta=ControlList['successBuyButton']
     
    
    # buyQuantityInfo=PictureInfo.OcrInfo.getKeyOfPosition("购买数量",260,5)
    # averageInfo=PictureInfo.OcrInfo.getKeyOfPosition("平均单价（近似值）",260,5)
    successBuyButtonPosition=None
    buyQuantityPosition=None
    averagePosition=None
    buyQuantitySuccessButtonPosition=None
   
    
    if buyQuantityMeta["init"]==True and buyQuantityMeta["allowCache"]==True:
        buyQuantityPosition=buyQuantityMeta["position"]
    else:
        buyQuantityPosition=PictureInfo.OcrInfo.getKeyOfPosition("购买数量",260,5)
        buyQuantityMeta["init"]=True
        buyQuantityMeta["position"]=buyQuantityPosition
        
    if averageMeta["init"]==True and averageMeta["allowCache"]==True:
        averagePosition=averageMeta["position"]
    else:
        averagePosition=PictureInfo.OcrInfo.getKeyOfPosition("平均单价（近似值）",260,5)
        averageMeta["init"]=True
        averageMeta["position"]=averagePosition
         
        
    if buyQuantitySuccessButtonMeta["init"]==True and buyQuantitySuccessButtonMeta["allowCache"]==True:
        buyQuantitySuccessButtonPosition=buyQuantitySuccessButtonMeta["position"]
    else:
        buyQuantitySuccessButtonPosition=PictureInfo.OcrInfo.getKeyOfPosition("购买",30,5)
        buyQuantitySuccessButtonMeta["init"]=True
        buyQuantitySuccessButtonMeta["position"]=buyQuantitySuccessButtonPosition
     
    random_move(buyQuantityPosition[0],buyQuantityPosition[1])
    sp()
    pyautogui.click()
    pyautogui.doubleClick()
    pyautogui.press('backspace')
    pyautogui.typewrite(str(random.randint(5,10)), interval=random.uniform(0.2,0.5))
    
    random_move(averagePosition[0],averagePosition[1])
    sp()
    pyautogui.click()
    pyautogui.doubleClick()
    pyautogui.press('backspace',presses=random.randint(5,10),interval=0.1)
     
    pyautogui.typewrite(str(currentAllowBuyTrascation["info"][2]), interval=random.uniform(0.2,0.5))
    
    random_move(buyQuantitySuccessButtonPosition[0],buyQuantitySuccessButtonPosition[1])
    pyautogui.click()
    
    if successBuyButtonMeta["init"]==True and successBuyButtonMeta["allowCache"]==True:
        successBuyButtonPosition=successBuyButtonMeta["position"]
        random_move(successBuyButtonPosition[0],successBuyButtonPosition[1])
        pyautogui.click()
def ScanProductPricesAction():
    global currentAllowBuyTrascation
    clickFlushButton()
    buyButtonOfTrasctionInfo=ControlList["buyButtonOfTrasction"]
    info=PictureInfo.OcrInfo.textMap
    p=None
    currentAllowBuyTrascation["info"]=None
    for value in commodity_price.keys():
        
        if (value in info) and is_number(info[value][2])and(int(info[value][2])<commodity_price[value]):
            currentAllowBuyTrascation["info"]=info[value]
    if currentAllowBuyTrascation["info"]!=None:
      random_move(currentAllowBuyTrascation["info"][0]+offset_x,currentAllowBuyTrascation["info"][1]+offset_y)
      pyautogui.click()
      if buyButtonOfTrasctionInfo["init"]==True and buyButtonOfTrasctionInfo["allowCache"]==True:
        p=buyButtonOfTrasctionInfo["position"]
        random_move(p[0],p[1])
        pyautogui.click()
        buyQuantityMeta=ControlList["buyQuantity"]
        averageMeta=ControlList["average"]
        buyQuantitySuccessButtonMeta=ControlList["buyQuantitySuccessButton"]
        successBuyButtonMeta=ControlList['successBuyButton']
        if buyQuantityMeta["init"]==True and buyQuantitySuccessButtonMeta["init"]==True and successBuyButtonMeta["init"]==True and averageMeta['init']==True:
          PurchaseGoodsActions()
          PurchaseGoodsSuccessAction()
      else:
        position=PictureInfo.OcrInfo.getKeyOfPosition("购买",30,10)
        buyButtonOfTrasctionInfo["init"]=True
        buyButtonOfTrasctionInfo["position"]=position
        p=buyButtonOfTrasctionInfo["position"]
        random_move(p[0],p[1])
        pyautogui.click()
       
    
def openTrascationActions():
    print("打开交易所")
    global currentTrascationPageOpen
    if currentTrascationPageOpen==False:
        currentTrascationPageOpen=True
        pyautogui.hotkey("alt","e")
        POcr.picture()
        info=PictureInfo.OcrInfo.textMap
        position=PictureInfo.OcrInfo.getKeyOfPosition("关注目录",30,10)
        random_move(position[0],position[1])
        pyautogui.click()

def PurchaseGoodsSuccessAction():
    successBuyButtonMeta=ControlList['successBuyButton']
    successBuyButtonPosition=None
    if successBuyButtonMeta["init"]==True:
        successBuyButtonPosition=successBuyButtonMeta["position"]
    else:
        successBuyButtonPosition=PictureInfo.OcrInfo.getKeyOfPosition("确认",30,5)
        successBuyButtonMeta["position"]=successBuyButtonPosition
        successBuyButtonMeta["init"]=True
    random_move(successBuyButtonPosition[0],successBuyButtonPosition[1])
    pyautogui.click()

def warnDialog():
    print("进入警告")
    cancelButtonPosition=PictureInfo.OcrInfo.getKeyOfPosition("取消",30,5)
    random_move(cancelButtonPosition[0],cancelButtonPosition[1])
    pyautogui.click()
    pyautogui.hotkey("esc")
     

ActionMap={
    "ScanProductPricesAction":ScanProductPricesAction,
    "PurchaseGoodsAction":PurchaseGoodsActions,
    "PurchaseGoodsSuccessAction": PurchaseGoodsSuccessAction,
    "openTrascationAction":openTrascationActions,
    "warnDialog":warnDialog
}
 