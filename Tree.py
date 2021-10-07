class Tree():
    def __init__(self):
        self.data = {}
    
    def addSingle(self,key,value):
        self.data.update({key: value})
    def addData(self, keyAndVal):
        self.data.update(keyAndVal)
    def showData(self):
        print(self.data.items())
    def navigate(self,keys = []):
        current = self.data
        for x in keys:
            current = current.get(x)
        return current

options = Tree()



