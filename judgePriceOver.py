import redis
import TransactionScreenOcr
import ocr
import time
from mouseMove import move,random_move
import pyautogui
from window import activeWindow
 
print(activeWindow)
r = redis.Redis(host='localhost', port=6379, db=0)
 
# TransactionScreenOcr.sceen(780,145,885,170,'money')
# r = redis.Redis()
# r.publish('channel', 'Hello from script 1')

messageId="14"
 
while True:
   time.sleep(15)
   TransactionScreenOcr.sceen(1046,788,1084,811,"./moneyOver.png")
   result=ocr.ocr('./moneyOver.png')[0]
   if isinstance(int(result),(int,float)):
       r.hset('goodsHash','priceOver',messageId)
       time.sleep(30)
       
    
        
    
   