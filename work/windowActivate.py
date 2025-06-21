 
import pyautogui
 
import pygetwindow as gw

def find_window_by_title(partial_title):
    for window in gw.getAllWindows():
        if partial_title in window.title:
            return window
    return None
activeWindow=find_window_by_title("命运")
pyautogui.FAILSAFE = False
activeWindow.activate()