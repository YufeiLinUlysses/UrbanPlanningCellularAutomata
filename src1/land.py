import cell as c
import numpy as np
import random
import landtype as lt
import math


class Land:
    row = 0
    col = 0
    land = []
    digitLand = []
    landTypes = [lt.Nature(), lt.Residential(),
                 lt.Commercial(), lt.Industrial()]
    landUseCount = [0, 0, 0, 0]
    collectTypes = {
        "Nature": [],
        "Residential": [],
        "Commercial": [],
        "Industrial": []
    }

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

    def collectLandUse(self):
        for i in range(self.row):
            for j in range(self.col):
                typeNum = self.digitLand.item((i, j))
                if typeNum == 0:
                    self.collectTypes["Nature"].append((i, j))
                elif typeNum == 1:
                    self.collectTypes["Residential"].append((i, j))
                elif typeNum == 2:
                    self.collectTypes["Commercial"].append((i, j))
                else:
                    self.collectTypes["Industrial"].append((i, j))

    def generateOriginalLand(self):
        rng = np.random.default_rng()
        randomArray = np.random.randint(4, size=(40))
        res = np.repeat(1, 30)
        na = np.repeat(0, 30)
        integrate = np.append(res, na)
        integrate = np.append(integrate, randomArray)
        result = np.reshape(integrate, (10, 10))
        rng.shuffle(integrate)
        result = np.reshape(integrate, (10, 10))

        # Define Center of the city, 4 commercial areas
        result.itemset((5, 2), 2)
        result.itemset((6, 2), 2)
        result.itemset((5, 3), 2)
        result.itemset((6, 3), 2)
        return result

    def __init__(self, row, col, land=None, digitland=None):
        self.row = row
        self.col = col
        self.digitland = self.generateOriginalLand()
        for digitRow in self.digitland:
            thisrow = []
            for ele in digitRow:
                self.landUseCount[ele] += 1
                elem = c.Cell(self.landTypes[ele])
                thisrow.append(elem)
            self.land.append(thisrow)
        self.updateInfo()
        self.digitLand = np.matrix(self.digitland)
        self.collectLandUse()
        # if land != None and digitland != None:
        #     self.land = land
        #     self.digitLand = digitland
        # else:
        #     self.digitland = GenerateOriginalLand()
        #     for digitRow in self.digitland:
        #         thisrow = []
        #         print(digitRow)
        #         for ele in digitRow:
        #             print(ele)
        #             self.landUseCount[ele] += 1
        #             elem = c.Cell(self.landTypes[ele])
        #             thisrow.append(elem)
        #         self.land.append(thisrow)
        # self.updateInfo()
        # self.collectLandUse()

    def newGen(self):
        self.landUseCount = [0, 0, 0, 0]
        self.collectTypes = {
            "Nature": [],
            "Residential": [],
            "Commercial": [],
            "Industrial": []
        }
        for i in range(self.row):
            for j in range(self.col):
                self.land[i][j] = self.land[i][j].update(
                    self.landTypes, self.land[i][j].landType.typeNum)
                num = self.land[i][j].landType.typeNum
                self.digitLand.itemset(
                    (i, j), num)
                self.landUseCount[num] += 1
        self.digitLand.itemset((5, 2), 2)
        self.digitLand.itemset((6, 2), 2)
        self.digitLand.itemset((5, 3), 2)
        self.digitLand.itemset((6, 3), 2)
        self.collectLandUse()
        self.updateInfo()
        return self

    def checkPercentage(self):
        total = self.col * self.row
        ans = "Percent of Nature: " + \
            str(round(self.landUseCount[0]/total * 100, 2)) + "\n"
        ans += "Percent of Residential: " + \
            str(round(self.landUseCount[1]/total * 100, 2)) + "\n"
        ans += "Percent of Commercial: " + \
            str(round(self.landUseCount[2]/total * 100, 2)) + "\n"
        ans += "Percent of Industrial: " + \
            str(round(self.landUseCount[3]/total * 100, 2)) + "\n"
        return ans

    def getShortestDist(self, i, j, landType):
        dist = 0
        count = 0
        for item in self.collectTypes[landType]:
            row = (item[0]-i)**2
            col = (item[1]-j)**2
            if count == 0:
                dist = math.sqrt(row + col)
                count += 1
            else:
                if math.sqrt(row + col) < dist:
                    dist = math.sqrt(row + col)
                    count += 1
        return dist

    def distAssess(self):
        dists = [0, 0, 0, 0]
        result = ""
        for key, val in self.collectTypes.items():
            for item in val:
                dists[0] += self.getShortestDist(item[0],
                                                 item[1], "Nature")
                dists[1] += self.getShortestDist(item[0],
                                                 item[1], "Residential")
                dists[2] += self.getShortestDist(item[0],
                                                 item[1], "Commercial")
                dists[3] += self.getShortestDist(item[0],
                                                 item[1], "Industrial")

            result += "Average Distance from "+key+"\n" +\
                "To Nature: " + \
                str(round(dists[0]/len(val), 2)) + "\n" +\
                "To Residential: " + \
                str(round(dists[1]/len(val), 2)) + "\n" +\
                "To Commercial: " + \
                str(round(dists[2]/len(val), 2)) + "\n" +\
                "To Industrial: " + \
                str(round(dists[3]/len(val), 2)) + "\n"

            dists = [0, 0, 0, 0]
        return result

    def sustanabilityAssessment(self, index=None):
        result = ""
        if index != None:
            result += "Generation " + str(index) + "\n"

        result += self.checkPercentage()
        result += self.distAssess()
        return result


# l = Land(3, 3)
# print(l.digitLand)
# print(l.collectTypes)
# temp = l.newGen()
# print(temp.digitLand)
# print(temp.collectTypes)

l = Land(10, 10)
