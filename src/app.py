from simpleland import SimpleLand
from land1 import Land1
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def GenerateOriginalLand():
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


def simpleLandTest():
    # Initialize plot
    fig, ax = plt.subplots()

    # Look at the change over a period of time
    generations = 10

    # Transition Matrix
    transit = np.matrix([
        [0.6, 0.1, 0.15, 0.15],
        [0.05, 0.8, 0.1, 0.05],
        [0.05, 0.15, 0.7, 0.1],
        [0.08, 0.02, 0.1, 0.8]
    ])

    # Initialize a land
    l = SimpleLand(10, 10, 4, transit, land=GenerateOriginalLand())
    im = ax.imshow(l.land)
    im.figure.savefig("../output/Original.png")

    for i in range(generations):
        fileName = "../output/Gen-"+str(i+1)+".png"
        l = l.withTransitionMatrix()
        heat = ax.imshow(l.land)
        heat.figure.savefig(fileName)


def land1Test():
    # Initialize plot
    fig, ax = plt.subplots()

    # Look at the change over a period of time
    generations = 10

    # Initialize a land
    l = Land1(10, 10)
    im = ax.imshow(l.digitLand)
    im.figure.savefig("../output/Land1-Original.png")

    for i in range(generations):
        fileName = "../output/Land1-Gen-"+str(i+1)+".png"
        l = l.newGen()
        heat = ax.imshow(l.digitLand)
        heat.figure.savefig(fileName)
        break


simpleLandTest()
# land1Test()
