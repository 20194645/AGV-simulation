# -*- coding: utf-8 -*-
from collections import deque
from model.utility import utility
class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
            
    def update(self,currentpos,nextpos,realtime):
        list = utility()
        del self.matrix[currentpos,nextpos]
        Q = deque()
        Q.append(nextpos)
        while Q:
            pos = Q[0]
            Q.pop()
            for i in list.findid(pos):
                if (pos,i) in self.matrix:
                    del self.matrix[pos,i]
                    Q.append(i)
        nextpos = list.M*(int(currentpos/list.M)+ realtime) + list.getid(nextpos)
        self.matrix[currentpos,nextpos] = realtime
        Q.append(nextpos)
        while Q:
            pos = Q[0]
            Q.pop()
            for i in list.findid(pos):
                if (pos,i) not in self.matrix:
                    self.matrix[pos,i] = int((pos-i)/list.M)
                    Q.append(i)      

    def writefile(self,startpos,inAGV):
        with open("TSG.txt", "w") as file:
            size = len(self.matrix)
            file.write("p min 82800 "+str(size)+"\n")
            file.write("n "+str(startpos)+" "+str(inAGV)+"\n")
            file.write("n "+str(82800)+str(0-inAGV)+"\n")
            for (i,j) in self.matrix:
                file.write("a "+str(i)+" "+str(j)+" 0 1 "+str(self.matrix[i, j]) + "\n")