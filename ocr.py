import pytesseract
from PIL import Image

# 指定 tesseract 可执行文件的路径（如果没有配置环境变量）
 

# 加载图像

def ocr(imageUrl="./image.png"):
    image = Image.open(imageUrl)

    # 识别文本，指定语言为中文（chi_sim）和英语（eng）
    text = pytesseract.image_to_string(image, lang='chi_sim+eng')
    list=text.split('\n')
    print(list)
    return  [item for item in list if item]



ocr()
