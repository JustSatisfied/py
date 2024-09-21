import redis
import TransactionScreenOcr
import ocr
import time
import pygetwindow as gw
r = redis.Redis(host='localhost', port=6379, db=0)

def find_window_by_title(partial_title):
    for window in gw.getAllWindows():
        if partial_title in window.title:
            return window
    return None
 
 
partial_title = "命运" 
window = find_window_by_title(partial_title)

# TransactionScreenOcr.sceen(780,145,885,170,'money')
# r = redis.Redis()
# r.publish('channel', 'Hello from script 1')

messageId="13"

while True:
   window.activate()
   time.sleep(2)
   TransactionScreenOcr.sceen(780,145,885,170,"./money.png")
   result=ocr.ocr('./money.png')
   if "," not in result[0]:
        r_id=redis.sadd('money',messageId)
        
    
   