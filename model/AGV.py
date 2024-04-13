class AGV:
    def __init__(self,id,prepos):
        self.id = id
        self.prepos = prepos
    def updatepos(self,pos):
        self.prepos = pos