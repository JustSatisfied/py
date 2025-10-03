import mss
import pygetwindow as gw
import time
import pyautogui
def screenshot_window(window_title):
    """
    根据窗口标题获取窗口，并截取其显示内容。
    :param window_title: 想要截取的应用程序窗口标题。
    """
    try:
        # 1. 找到指定标题的窗口
        window = gw.getWindowsWithTitle(window_title)[0]
        
        # 2. 激活窗口，确保其在最前台，防止被其他窗口遮挡
        if not window.isActive:
            window.activate()
        
        # 3. 添加短暂延迟，让窗口有时间完全渲染到前台
         
        
        # 4. 获取窗口的精确坐标和尺寸
        x, y, width, height = window.left, window.top, window.width, window.height
        
        # 5. 使用 mss 截取指定区域
        with mss.mss() as sct:
            monitor = {"top": y, "left": x, "width": width, "height": height}
            screenshot = sct.grab(monitor)
            
            # 6. 保存截图
            output_path = f"{window_title}_screenshot.png"
            mss.tools.to_png(screenshot.rgb, screenshot.size, output=output_path)
            print(f"成功截取窗口 '{window_title}' 并保存为 {output_path}")

    except IndexError:
        print(f"错误：未找到窗口 '{window_title}'。请确保应用程序正在运行。")
    except Exception as e:
        print(f"截取窗口失败：{e}")

# 示例：截取“记事本”窗口（请确保该程序正在运行）
screenshot_window("梦幻")

while True:
    time.sleep(15)
    screenshot_window("梦幻")
    pyautogui.click()
    pyautogui.hotkey('alt', '=') 