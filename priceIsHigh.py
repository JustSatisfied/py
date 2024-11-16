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

messageId="15"


while True:
   time.sleep(15)
   TransactionScreenOcr.sceen(2973,750,3186,811,"./priceIsHigh.png")
   result=ocr.ocr('./priceIsHigh.png')[0]
   for result in str:
       if "高于" in str:  
        r.hset('goodsHash','priceIsHigh',messageId)
 
       