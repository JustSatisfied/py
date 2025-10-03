from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
 
import os
# 初始化 PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

def Ocr(img_path):
    # 指定图像路径
    # 进行文字识别
    current_script_path = os.path.abspath(__file__)
    current_script_dir = os.path.dirname(current_script_path)
    dir_path=os.path.join(current_script_dir,img_path)
  
    print(f"DEBUG: Ocr function is trying to process image at: {dir_path}")
    result = ocr.ocr(dir_path, cls=True)
    bbox=[]
    text=[]
    confidence=[]
    # 打印包含位置信息的识别结果
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            # line 的结构通常是 [((x1, y1), (x2, y2), (x3, y3), (x4, y4)), ('文本内容', 置信度)]
            bbox.append(line[0])  # 文本框的坐标
            text.append(line[1][0])  # 识别的文本内容
            confidence.append(line[1][1])  # 置信度
           
     
    textMap={}
   
    for index,value in enumerate(text):
        position=bbox[index]
        if value in textMap:
            textMap[value+"副本"]=[position[0][0],position[0][1]]
        else:
            position=bbox[index]
            textMap[value]=[position[0][0],position[0][1]]
            if index+3<=len(text)-1:
             textMap[value].append(text[index+3])
    
    # if result and len(result) > 0:
    #     image = Image.open(absolute_path).convert('RGB')
    #     boxes = [line[0] for line in result[0]]
    #     txts = [line[1][0] for line in result[0]]
    #     scores = [line[1][1] for line in result[0]]
    #     im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
    #     im_show = Image.fromarray(im_show)
    #     im_show.save('result.jpg')
    # else:
    #     print("未检测到任何文本。")
     
    return [bbox,text,confidence,textMap]
 