import time




class transcation:
    def __init__(self,flag):
        self.flag = flag
        self.currentFlush=0
        self.activate=False
    def close(self):
        self.flag=False
    def open(self):
        self.flag=True
    def addCurrentFlush(self):
        print(self.currentFlush)
        if(self.currentFlush==5):
            self.currentFlush=0
            time.sleep(random.randint(120,720))
        else:
            self.currentFlush+=1
    def openActivate(self):
        self.activate=True
    def closeActivate(self):
        self.activate=False