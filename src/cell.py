from collections import deque
import numpy as np
import landType as lt
from rule import Rule
import random


class Cell:
    landUseCount = {}
    landType = None
    record = deque([lt.Nature() for i in range(5)])
    prob = 0

    def __init__(self, landType):
        self.landType = landType
        self.record.append(landType)
        self.record.popleft()
        self.landUseCount = {
            "Nature": 4,
            "Residential": 0,
            "Commercial": 2,
            "Industrial": 2
        }
        self.prob = random.random()        

    def update(self):
        prob = self.prob
        rules = self.landType.rules
        for i in range(len(rules)):
            cur = rules[i].rule(self)
            if (cur is True):
                tempProbs = rules[i].probs
                for j in range(len(tempProbs)):
                    if prob > tempProbs[j]:
                        prob = prob-tempProbs[j]
                    else:
                        newType = assignType(j)
                        return Cell(newType)

def assignType(result):
    if result == 0:
        return lt.Nature()
    elif result == 1:
        return lt.Residential()
    elif result == 2:
        return lt.Commercial()
    return lt.Industrial()

# c =Cell(lt.Nature())
# print(c.landType.typeName)
# c=c.update()
# print(c.landType.typeName)
