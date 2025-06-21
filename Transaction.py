import random
import time
import random;
import pyautogui
 
step = 20
start_pos = (200, 200)  # 起始坐标
target_pos = (1351, 45)  # 终点坐标

def move(start_pos,target_pos,step=random.randint(20,35),relative_pos_list=[]):
        def move_pos(start_pos, target_pos, step=10):
            
            for i in range(0, step):
                if i <= step / 2:
                    dx = int(random.random() * (target_pos[0] - start_pos[0]) / step)
                    dy = int(random.random() * (target_pos[1] - start_pos[1]) / step)
                else:
                    dx = int(random.random() * (target_pos[0] - start_pos[0]) / step * 2)
                    dy = int(random.random() * (target_pos[1] - start_pos[1]) / step * 2)
                # time.sleep(random.random() * 0.001)
               
                relative_pos_list.append((dx, dy))


            move_pos(start_pos, target_pos, step)
            pyautogui.moveTo(start_pos)  
            for pos in relative_pos_list:  
             pyautogui.move(pos)
            pyautogui.moveTo(target_pos)  

