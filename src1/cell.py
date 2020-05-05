from collections import deque
import numpy as np
import landtype as lt
import random
import rules


class Cell:
    landUseCount = {
        "Nature": 0,
        "Residential": 0,
        "Commercial": 0,
        "Industrial": 0
    }
    landUseDist = {
        "Nature": 0,
        "Residential": 0,
        "Commercial": 0,
        "Industrial": 0
    }
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

    def update(self, landTypes, typeNum):
        # Update Probabilities for each different land use types
        nature = self.landUseCount["Nature"]
        residential = self.landUseCount["Residential"]
        commercial = self.landUseCount["Commercial"]
        industrial = self.landUseCount["Industrial"]
        total = nature + residential + commercial + industrial
        allNature = rules.AllNature()
        allResidential = rules.AllResidential()
        allCommercial = rules.AllCommercial()
        allIndustrial = rules.AllIndustrial()
        probs = nature/total*allNature.probs[0] + \
            residential/total * allResidential.probs[0] + \
            commercial/total * allCommercial.probs[0] + \
            industrial/total*allIndustrial.probs[0]
        prob = random.random()

        for i in range(4):
            if prob > probs.item(i):
                prob = prob-probs.item(i)
            else:
                newType = landTypes[i]
                return Cell(newType)
