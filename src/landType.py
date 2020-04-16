from rule import Rule


class LandType:
    typeName = ""
    typeNum = -1
    rules = []

    def __init__(self, name, num, rules):
        self.typeName = name
        self.typeNum = num
        self.rules = rules


# Nature land use type rule
def Nature():

    # Stays the same
    srule1 = Rule(rule=lambda cell: cell.landUseCount["Nature"] <= 2,
                  probs=[1, 0, 0, 0])
    srule2 = Rule(rule=lambda cell: cell.landUseCount["Nature"] >= 7,
                  probs=[1, 0, 0, 0])

    # Change to other types
    orule1 = Rule(rule=lambda cell: cell.landUseCount["Commercial"] >= 3,
                  probs=[0.2, 0.3, 0.4, 0.1])
    orule2 = Rule(rule=lambda cell: cell.landUseCount["Industrial"] >= 5,
                  probs=[0.1, 0, 0.3, 0.6])

    # General
    general = Rule(rule=lambda cell: True, probs=[0.7, 0.1, 0.1, 0.1])

    rules = [srule1, srule2, orule1, orule2, general]

    nature = LandType(name="Nature",
                      num=0,
                      rules=rules)

    return nature

# Residential land use type rule
def Residential():

    # Stays the same
    srule1 = Rule(rule=lambda cell: cell.landUseCount["Industrial"] <= 1,
                  probs=[0, 1, 0, 0])
    srule2 = Rule(rule=lambda cell: cell.landUseCount["Commercial"] + cell.landUseCount["Nature"] >= 5,
                  probs=[0, 1, 0, 0])

    # Change to other types
    orule1 = Rule(rule=lambda cell: cell.landUseCount["Commercial"] >= 3 and cell.landUseCount["Commercial"] + cell.landUseCount["Nature"] < 5,
                  probs=[0.1, 0.5, 0.3, 0.1])
    orule2 = Rule(rule=lambda cell: cell.landUseCount["Residential"] >= 5,
                  probs=[0.6, 0.2, 0.2, 0])
    orule3 = Rule(rule=lambda cell: cell.landUseCount["Industrial"] >= 5,
                  probs=[0.6, 0.2, 0.2, 0])

    # General
    general = Rule(rule=lambda cell: True, probs=[0.3, 0.4, 0.3, 0])

    rules = [srule1, srule2, orule1, orule2, orule3, general]

    residential = LandType(name="Residential",
                           num=1,
                           rules=rules)

    return residential

# Commercial land use type rule
def Commercial():

    # Stays the same
    srule1 = Rule(rule=lambda cell: cell.landUseCount["Residential"] >= 2,
                  probs=[0, 0, 1, 0])

    # Change to other types
    orule1 = Rule(rule=lambda cell: cell.landUseCount["Residential"] >= 1 and cell.landUseCount["Nature"] >=1,
                  probs=[0.15, 0.35, 0.45, 0.05])
    orule2 = Rule(rule=lambda cell: cell.landUseCount["Industrial"] >= 3,
                  probs=[0.1, 0, 0.6, 0.3])
    orule3 = Rule(rule=lambda cell: cell.landUseCount["Residential"] >= 3,
                  probs=[0.3, 0.4, 0.3, 0])

    # General
    general = Rule(rule=lambda cell: True, probs=[0.2, 0.4, 0.3, 0.1])

    rules = [srule1, orule1, orule2, orule3, general]

    commercial = LandType(name="Commercial",
                           num=2,
                           rules=rules)

    return commercial

# Industrial land use type rule
def Industrial():

    # Stays the same
    srule1 = Rule(rule=lambda cell: cell.landUseCount["Industrial"] <= 4,
                  probs=[0, 0, 0, 1])
    srule2 = Rule(rule=lambda cell: cell.landUseCount["Residential"] <= 3,
                  probs=[0, 0, 0, 1])

    # Change to other types
    orule1 = Rule(rule=lambda cell: cell.landUseCount["Nature"] >= 4 and cell.landUseCount["Residential"] <= 3,
                  probs=[0.3, 0, 0.2, 0.5])

    # General
    general = Rule(rule=lambda cell: True, probs=[0.2, 0.1, 0.3, 0.4])

    rules = [srule1, srule2, orule1, general]

    commericial = LandType(name="Industrial",
                           num=3,
                           rules=rules)

    return commericial
