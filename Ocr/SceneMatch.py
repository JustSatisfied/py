
TransicationPage="Other"
BuyingProcess="购买数量"
BuySuccess="确认"



class Scene:
    def __init__(self,name,ControlArray):
        self.current=name
        self.ControlArray=ControlArray
    def defaultMatchFc(self,titleResult):
        for titleIndex,titleValue in enumerate(titleResult):
            if titleValue==self.current:
                return True
        return False
    def operatorControlArray(self,opFc):
         self.ControlArray=opFc(self)
    def getSceneControlArray(self):
        return self.ControlArray
    def isMatch(self,titleResult,fc):
        if fc==None:
           self.defaultMatchFc(self,titleResult)
        else:
           fc(self,titleResult)