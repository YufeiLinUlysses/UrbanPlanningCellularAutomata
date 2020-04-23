from collections import deque
import numpy as np
import landType as lt
from rule import Rule
import random


class Cell:
    landUseCount = {}
    landType = None
    record = deque([lt.Nature() for i in range(5)])
    probs = [0, 0, 0, 0]
    prob = 0

    def __init__(self, landType):
        self.landType = landType
        self.record.append(landType)
        self.record.popleft()
        self.landUseCount = {
            "Nature": 0,
            "Residential": 0,
            "Commercial": 0,
            "Industrial": 0
        }
        self.prob = random.random()

    def update(self):
        prob = self.prob
        probs = self.probs 
        for i in range(len(probs)):
            if prob > probs[i]:
                prob = prob-probs[i]
            else:
                newType = assignType(i)
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
