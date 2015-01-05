'''
Created on Apr 17, 2014

@author: Brendan
'''


def blocks(x,y):
    if(x<=2):
        if(y<=2):
            return (0,0)
        if(y<=5):
            return (0,3)
        if(y<=8):
            return (0,6)
    if(x<=5):
        if(y<=2):
            return (3,0)
        if(y<=5):
            return (3,3)
        if(y<=8):
            return (3,6)
    if(x<=8):
        if(y<=2):
            return (6,0)
        if(y<=5):
            return (6,3)
        if(y<=8):
            return (6,6)
        
        
        
class cell():

    def __init__(self, number):
        self.possibleNums = [1,2,3,4,5,6,7,8,9]
        self.currentNum = str(number)
        self.done = False
        if(int(number) != 0):
            self.done = True
            self.possibleNums = []
        
    
    def __str__(self):
        return self.currentNum
    
    def __repr__(self):
        return str(self.currentNum)
    
    def getNums(self):
        return self.possibleNums
    
    def getNum(self):
        return int(self.currentNum)
    
    def isDone(self):
        return self.done
    
    def setDone(self):
        self.done = True
        self.possibleNums = []
    
    def setNumber(self):
        self.currentNum = self.possibleNums[0]
        self.done = True
        self.possibleNums = []
        
    def getNumsLength(self):
        return len(self.possibleNums)
    
    def setPossibleNum(self, a):
        self.possibleNums = [a]
        self.done = True
        self.currentNum = a
        
    def setPossibleNumList(self, lists):
        self.possibleNums = lists
    
class puzzle:
        
    def len(self):
        return 9
    
    def __str__(self):
        return self.rows   

    row0=[]
    row1=[]
    row2=[]
    row3=[]
    row4=[]
    row5=[]
    row6=[]
    row7=[]
    row8=[]

    rows = [row0,row1,row2,row3,row4,row5,row6,row7,row8] 
         
    for i in range(len(rows)):
    
        listlist = input("Type the first row:")

        if(len(listlist) != 9):
            print("list is not 9 digits long")
        for j in range(9):    
            rows[i].append(cell(listlist[j]))
    print("ORIGINAL:")
    for i in range(len(rows)):
        print(rows[i])
    print()
       
        
    

def sudoku():
    a = puzzle()
    
    for cocks in range(400):
        for i in range(a.len()):
            for j in range(len(a.rows)):
                currentCell = a.rows[i][j]
                if i == 6 and j == 0:
                    pass
                if(currentCell.isDone() == False):
                    possibleNums = (currentCell.getNums())
                    
                    
                    """Checks in same row"""
                    megaNums = []
                    for k in range(9):
                        
                        if j != k:
                            checkCell = a.rows[i][k]
                            if checkCell.isDone() == False:                            
                                for v in range(len(checkCell.getNums())):
                                    megaNums.append(checkCell.getNums()[v])
                            else:
                                try:
                                    possibleNums.remove(checkCell.getNum())
                                except:
                                    pass
                        
                    
                    if cocks > 0:
                        xyz = set(megaNums)
                        xy = set(possibleNums)
                        z = xy - xyz
                        z = list(z)
                        if len(z) == 1:
                            currentCell.setPossibleNum(z[0])
                         
                                
                    
                    """Checks in same column""" 
                    megaNums = []        
                    for m in range(9):
                        if i != m:
                            checkCell = a.rows[m][j]
                            if checkCell.isDone() == False:
                                for v in range(len(checkCell.getNums())):
                                    megaNums.append(checkCell.getNums()[v])
                            else:
                                try:
                                    possibleNums.remove(checkCell.getNum())
                                except(ValueError):
                                    pass
                    
                    
                    if cocks > 0:
                        xyz = set(megaNums)
                        xy = set(possibleNums)
                        z = xy - xyz
                        z = list(z)
                        if len(z) == 1:
                            currentCell.setPossibleNum(z[0])
                            
                            
                    
                    
                    startingPoint = blocks(i,j)
                    xStart = startingPoint[0]
                    yStart = startingPoint[1]
                
                    """Checks Boxes"""
                    for x in range (xStart, xStart+3):
                        for y in range(yStart, yStart+3):
                            if (x != i) and (y != j):
                                    checkCell = a.rows[x][y]
                                    if checkCell.isDone() == False:
                                        for v in range(len(checkCell.getNums())):
                                            megaNums.append(checkCell.getNums()[v]) 
                                    else:
                                        try:
                                            possibleNums.remove(checkCell.getNum())
                                        except(ValueError):
                                            pass
                                        
                                        
                    
                    if cocks > 0:
                        xyz = set(megaNums)
                        xy = set(possibleNums)
                        z = xy - xyz
                        z = list(z)
                        if len(z) == 1:
                            currentCell.setPossibleNum(z[0])        
                            
                    currentCell.setPossibleNumList(possibleNums)          
                    
                                    
                    if(possibleNums == 1):
                        currentCell.setDone()
                        currentCell.setNumber()

            
                
                    
                    
                        
    print("Solved:")
    for i in range(len(a.rows)):
                
        print(a.rows[i])

    input("press enter")


sudoku()
