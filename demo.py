from google import genai
import mss
from PIL import Image
import window
import pyautogui
import time
# pyautogui.FAILSAFE = False
# window.activeWindow.activate()
# time.sleep(1)
with mss.mss() as sct:
    # 获取屏幕信息
    monitor = sct.monitors[1]  # monitors[0] 是所有屏幕的合并，monitors[1] 是主屏幕

    # 定义截图区域（整个屏幕）
    left = monitor["left"]
    top = monitor["top"]
    width = monitor["width"]
    height = monitor["height"]
    bbox = (left, top, width, height)

    # 截图
    sct_img = sct.grab(bbox)

    # 将截图数据转换为 PIL Image 对象
    img = Image.frombytes("RGB", sct_img.size, sct_img.rgb, "raw", "RGB", 0, 1)

    # 保存图片
    img.save("./screen.png")
    
    
client = genai.Client(api_key="AIzaSyCwQ7YVspU9GB7fWEtj0d9mJlnqgNV9swo")

my_file = client.files.upload(file="./demo.png")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[my_file, "丰饶之间是否完成图片中，红点代表未完成 只需要回答完成或者未完成 丰饶之间这4个字的坐标是多少 你得坐标是怎么测算的 为什么感觉会偏小很多"],
)

print(response.text)