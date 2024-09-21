import redis
import time
from mouseMove import random_move
import pyautogui
r=redis.Redis(host="localhost",port=6379,db=0)

def getHashHandle():
     if r.hexists("goodsPrice","goodsPrice"):
         pyautogui.press("esc")
         pyautogui.press("esc")
         r.hdel("goodsPrice","goodsPrice")

