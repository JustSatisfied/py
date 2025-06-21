
class SceneControl:
    def __init__(self,name):
        self.name=name 
        self.x=0
        self.y=0
    
    def offset(self,x,y):
        self.x=x;
        self.y=y
    