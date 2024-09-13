import random
import time
import pyautogui
import math;
 

def move(start_pos, end_pos, duration=random.uniform(0,1)):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    steps = random.randint(5,10)  # 可以增加这个值来使曲线更平滑
 
    # 生成随机的时间间隔，并按升序排列
    time_intervals = sorted([random.random() for _ in range(steps)])
    
    # 计算每一步的时间间隔
    step_duration = duration / len(time_intervals)

    for i, t in enumerate(time_intervals):
        # 计算当前位置
        x = start_x + t * (end_x - start_x)
        y = start_y + t * (end_y - start_y)
        
        # 移动鼠标到计算出的坐标
        pyautogui.moveTo(x, y)
        
        # 随机延迟以模拟不规律的速度
        if i < len(time_intervals) - 1:
            # 计算下一步的时间间隔，以模拟不规律的速度
            next_step_duration = random.uniform(0.01, 0.05)
            time.sleep(next_step_duration)
    
    # 确保鼠标最终位置在 end_pos
    pyautogui.moveTo(end_x, end_y)
def random_move(x1,y1,x2,y2):
    x,y=random_x_y(x1,y1,x2,y2)
    px,py=pyautogui.position()
  
    move((px,py),(x,y))


def random_x_y(x1,y1,x2,y2):
    return (random.randint(x1,x2),random.randint(y1,y2))