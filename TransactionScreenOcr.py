 
from PIL import ImageGrab
import os
def sceen(x,y,x1,y1,imageUrl):
    region = (x,y,x1,y1)
    screenshot = ImageGrab.grab(bbox=region)
    screenshot.save(imageUrl)
    
 