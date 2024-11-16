import pyautogui
import time
import random
import sys
import traceback
import os
import redis
import pyautogui
import getRedis
from analysisGoodsImage import close
from datetime import datetime
from window import activeWindow as window
from trancationInstance import transcation 
from mouseMove import move,random_move
from main import main
 


r = redis.Redis(host='localhost', port=6379, db=0)
hset_key="goodsHash"

pyautogui.FAILSAFE = False
last_run_minute = None
transcation_=transcation(False)
window.activate()
 
def sp(st=0,et=1):
    time.sleep(random.uniform(st,et))

def should_run_task(now):
    minute = now.minute
    return (minute==random.randint(15,20)) or (minute==random.randint(30,35))
 
def process_main():
    while True:
        if r.hexists(hset_key,"priceIsHigh"):
            random_move(3080,940,3156,956)
            pyautogui.click()
            r.hdel(hset_key,"priceIsHigh")
        now=datetime.now()
        if should_run_task(now) and last_run_minute != now.minute:
            close(transcation_)
            # if transcation_==True:
            #     transcation_.closeActivate()
            last_run_minute = now.minute
            main(transcation_)
            continue
        else:
            sp(1,3)
            getRedis.getHashHandle()
            main(transcation_)
    
def global_exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        sys.exit(0)
        return
    print("全局捕获到未处理的异常，重新启动脚本:")
    if exc_type in {ValueError, IndexError}:
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        python = sys.executable  # 获取当前 Python 解释器路径
        os.execv(python, [python] + sys.argv)  # 重新执行脚本
    else:
        # 捕获其他异常时，打印并终止程序
        print("捕获到非特定异常，程序将终止:")
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        sys.exit(1)

sys.excepthook = global_exception_handler

 
process_main()