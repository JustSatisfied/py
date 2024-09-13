from ocr import ocr
import pyautogui
from PIL import ImageGrab

def sceen(x,y,x1,y1,imageUrl):
    region = (x,y,x1,y1)
    screenshot = ImageGrab.grab(bbox=region)
    screenshot.save(imageUrl)
    
    