import cell as c
import numpy as np
import random


class Land1:
    row = 0
    col = 0
    land = []
    digitLand = []

    def updateInfo(self):
        for i in range(self.row):
            for j in range(self.col):
                t = i-1
                b = i+1
                l = j-1
                r = j+1
                landType = self.land[i][j].landType.typeName

                # Current row
                if l >= 0:
                    self.land[i][l].landUseCount[landType] += 1
                if r < self.col:
                    self.land[i][r].landUseCount[landType] += 1

                # Upper row
                if t >= 0:
                    self.land[t][j].landUseCount[landType] += 1
                if t >= 0 and l >= 0:
                    self.land[t][l].landUseCount[landType] += 1
                if t >= 0 and r < self.col:
                    self.land[t][r].landUseCount[landType] += 1

                # Lower row
                if b < self.row:
                    self.land[b][i].landUseCount[landType] += 1
                if b < self.row and l >= 0:
                    self.land[b][l].landUseCount[landType] += 1
                if b < self.row and r < self.col:
                    self.land[b][r].landUseCount[landType] += 1

    def __init__(self, row, col, land=None, digitland=None):
        self.row = row
        self.col = col
        if land != None:
            self.land = land
        if digitland != None:
            self.digitLand = digitland
        else:
            for i in range(row):
                thisrow = []
                thisdigitrow = []
                for j in range(col):
                    typeNum = random.randint(0, 3)
                    newType = c.assignType(typeNum)
                    ele = c.Cell(newType)
                    thisrow.append(ele)
                    thisdigitrow.append(typeNum)
                self.land.append(thisrow)
                self.digitLand.append(thisdigitrow)
            self.updateInfo()
            self.digitLand = np.matrix(self.digitLand)

    def newGen(self):
        for i in range(self.row):
            for j in range(self.col):
                self.land[i][j] = self.land[i][j].update()
                self.digitLand.itemset((i,j), self.land[i][j].landType.typeNum)
        self.updateInfo()
        return self


# l = Land1(10, 10)
# print(l.digitLand)

# l = l.newGen()
# print(l.digitLand)
