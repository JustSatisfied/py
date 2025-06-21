 
    
import time
import subprocess
import sys
import os
from pynput import keyboard, mouse # 导入 pynput 模块

# 定义30分钟的空闲时间阈值（秒）
IDLE_THRESHOLD_SECONDS = 5 * 60 # 30 minutes

# 定义要执行的脚本的命令
# 请替换成你的实际 Python 脚本路径
# 使用 sys.executable 来确保使用当前 Python 解释器运行你的脚本
SCRIPT_TO_EXECUTE = [sys.executable, r"C:\Users\Administrator\Desktop\new\py\py\esc.py"] # <-- 修改为你的 Python 脚本路径

# 全局变量，记录最后一次物理输入的时间戳
last_physical_input_time = time.time()
print(os.getpid())
# -------------------------------------------------
# pynput 回调函数，用于更新最后输入时间戳
# -------------------------------------------------

def on_key_event(key):
  
    global last_physical_input_time
    last_physical_input_time = time.time()
    # print(f"键盘事件发生，更新时间: {last_physical_input_time}") # 调试用

def on_mouse_move(x, y):
    
    global last_physical_input_time
    last_physical_input_time = time.time()
    # print(f"鼠标移动发生，更新时间: {last_physical_input_time}") # 调试用

def on_mouse_click(x, y, button, pressed):
   
    global last_physical_input_time
    last_physical_input_time = time.time()
    # print(f"鼠标点击发生 ({'按下' if pressed else '释放'})，更新时间: {last_physical_input_time}") # 调试用

def on_mouse_scroll(x, y, dx, dy):
    
    global last_physical_input_time
    last_physical_input_time = time.time()
    # print(f"鼠标滚动发生，更新时间: {last_physical_input_time}") # 调试用

# -------------------------------------------------
# 主逻辑
# -------------------------------------------------
 

def main():
    print(f"开始监控物理输入，空闲 {IDLE_THRESHOLD_SECONDS // 60} 分钟后将执行脚本。")
    print(f"将要执行的命令: {' '.join(SCRIPT_TO_EXECUTE)}") # 打印即将执行的命令

    # 启动键盘监听器 (在一个单独的线程中运行)
    keyboard_listener = keyboard.Listener(on_press=on_key_event, on_release=on_key_event) # 监听按下和释放
    keyboard_listener.start()
    print("键盘监听器已启动。")

    # 启动鼠标监听器 (在一个单独的线程中运行)
    mouse_listener = mouse.Listener(on_move=on_mouse_move, on_click=on_mouse_click, on_scroll=on_mouse_scroll)
    mouse_listener.start()
    print("鼠标监听器已启动。")

    while True:
        global last_physical_input_time
        current_time = time.time()
        idle_seconds = current_time - last_physical_input_time

        # print(f"当前空闲时间: {int(idle_seconds)} 秒") # 可以取消注释用于调试
        # print(idle_seconds >= IDLE_THRESHOLD_SECONDS) # 调试用

        if idle_seconds >= IDLE_THRESHOLD_SECONDS:
            print(f"检测到物理空闲时间达到 {IDLE_THRESHOLD_SECONDS} 秒，执行脚本...")
            try:
                # 使用 subprocess 执行脚本
                # shell=False 更安全，直接运行指定的 Python 解释器和脚本
                subprocess.run(SCRIPT_TO_EXECUTE, shell=False, check=True)

                print("脚本执行完毕。")
                # 脚本执行后，可以暂停监控一段时间，或者直接退出，
                # 或者在下一次循环中继续监控。
                # 这里我们选择在脚本执行后等待一分钟，避免短时间内重复执行
                time.sleep(60)
                # 重置计时器，避免脚本执行后立即再次触发

                last_physical_input_time = time.time()
                print("等待一分钟后，计时器已重置，继续监控...")


            except subprocess.CalledProcessError as e:
                print(f"执行脚本时出错: {e}")
                print(f"错误输出:\n{e.stderr}")
            except FileNotFoundError:
                 print(f"错误: 找不到 Python 解释器或脚本文件 {SCRIPT_TO_EXECUTE}")
            except Exception as e:
                print(f"发生未知错误: {e}")

        # 每隔10秒检查一次，并给监听器线程处理事件的时间
        time.sleep(10)

    # 理论上循环会一直运行，如果需要优雅退出，可以添加信号处理
    # keyboard_listener.join()
    # mouse_listener.join()


if __name__ == "__main__":
    main()