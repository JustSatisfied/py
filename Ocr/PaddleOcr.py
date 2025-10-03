
from .screen import screen_config

from .ocr import Ocr
from PIL import ImageGrab
import random
import os

class PictureInfo:
    OcrInfo=None 
    def __init__(self,bbox,text,confidence,textMap) -> None:
        self.bbox=bbox
        self.text=text
        self.confidence=confidence
        self.textMap=textMap
    @staticmethod
    def getKeyOfPosition(name,x1,y1):
        p=PictureInfo.OcrInfo.textMap[name]
        offset_x=screen_config["offset_x"]
        offset_y=screen_config["offset_y"]
        x=p[0]+random.uniform (x1,x1+10)+offset_x
        y=p[1]+random.uniform(y1,y1+5)+offset_y
         
        return (x,y)
class POcr:
    @staticmethod
    def picture():
        
        path=screen_config['path']
        current_script_path = os.path.abspath(__file__)
        current_script_dir = os.path.dirname(current_script_path)
        dir_path=os.path.join(current_script_dir,path)
        
      
        offset_x=screen_config["offset_x"]
        offset_y=screen_config["offset_y"]
        ocr_screenX=screen_config["ocr_screenX"]
        ocr_screenY=screen_config['ocr_screenY']
        
        region = (offset_x,offset_y,ocr_screenX,ocr_screenY)
        screenshot = ImageGrab.grab(bbox=region)
        screenshot.save(dir_path)
        
        bbox,text,confidence,textMap=Ocr(path)
        PictureInfo.OcrInfo=PictureInfo(bbox,text,confidence,textMap)
       
    @staticmethod
    def getKeyOfPosition(name,offset_x,offset_y):
        PictureInfo.OcrInfo.getKeyOfPosition(name,offset_x,offset_y)

 