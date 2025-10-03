 
from Ocr.PaddleOcr import PictureInfo
from mouseMove import move,random_move
import pyautogui
import time
import random
from .action import ActionMap

            
def sp(st=0,et=1):
    time.sleep(random.uniform(st,et))
    
def openTrascationActions():
   pyautogui.hotkey("alt","y")
   sp(1,3)
   pyautogui.click()

 

    
 

   
ControlNotInSceneList={
    "openTrascation":{
        "sceneName":"openTrascation",
        "init":False,
        "lane":99,
        "action":ActionMap["openTrascationAction"],
        # "countinous":True,
        # "countinousStep":[
        #     "buyButton"
        # ],
        # "successActions":cacheTrascationButton,
        "notes":"判断是否打开了物品交易所",
        "math":"物品交易所",
        "validate":lambda info:"物品交易所" not in info,
        "allowCache":False,
    },
     "warnDialog":{
        "sceneName":"warnDialog",
        "action":ActionMap["warnDialog"],
        "validate":lambda info:"所选道具价格高于昨日平均交易价" in info,
    },
    "PurchaseGoods":{
        "sceneName":"PurchaseGoods",
        "math":"购买物品",
        "action":ActionMap["PurchaseGoodsAction"],
        "init":False,
        "notes":"购买物品",
        "validate":lambda info:"购买物品" in info,
        "allowCache":True,
    },
    "PurchaseGoodsSuccess":{
        "sceneName":"PurchaseGoodsSuccess",
        "action":ActionMap["PurchaseGoodsSuccessAction"],
        "init":False,
        "notes":"购买成功",
        "validate":lambda info:"购买成功" in info or "以其他价格购买成功" in info,
        "allowCache":True,
    },
    "ScanProductPrices": {
        "sceneName":"ScanProductPrices",
        # "successActions":ScanProductPricesAction,
        "lane":0,
        "action":ActionMap["ScanProductPricesAction"],
        "init":False,
        "validate":False,
        "notes":"扫描当前商品价格"
    },
     
}


print(PictureInfo)