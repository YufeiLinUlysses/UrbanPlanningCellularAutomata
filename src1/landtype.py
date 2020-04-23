class LandType:
    typeName = ""
    typeNum = -1

    def __init__(self, name, num):
        self.typeName = name
        self.typeNum = num


# Nature land use type rule
def Nature():
    nature = LandType(name="Nature",
                      num=0)
    return nature

# Residential land use type rule


def Residential():
    residential = LandType(name="Residential",
                           num=1)
    return residential

# Commercial land use type rule


def Commercial():
    commercial = LandType(name="Commercial",
                          num=2)
    return commercial

# Industrial land use type rule


def Industrial():
    industrial = LandType(name="Industrial",
                          num=3)
    return industrial
