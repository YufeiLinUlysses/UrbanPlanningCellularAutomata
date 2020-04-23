from collections import deque
import numpy as np
import landtype as lt
import random


class Cell:
    landUseCount = {}
    landType = None
    record = deque([lt.Nature() for i in range(5)])
    

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

    def update(self, landTypes):
        # Update Probabilities for each different land use types
        nature = self.landUseCount["Nature"]
        residential = self.landUseCount["Residential"]
        commercial = self.landUseCount["Commercial"]
        industrial = self.landUseCount["Industrial"]
        total = nature + residential + commercial + industrial
        probs = [
            nature/total,
            residential/total,
            commercial/total,
            industrial/total
        ]
        prob = random.random()

        for i in range(4):
            if prob > probs[i]:
                prob = prob-probs[i]
            else:
                newType = landTypes[i]
                return Cell(newType)
