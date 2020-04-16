from simpleland import SimpleLand
from land1 import Land1
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def simpleLandTest():
    # Initialize plot
    fig, ax = plt.subplots()

    # Look at the change over a period of time
    generations = 10

    # Transition Matrix
    transit = np.matrix([
        [0.4, 0.5, 0.7],
        [0.3, 0.5, 0.2],
        [0.3, 0, 0.1]
    ])

    # Initialize a land
    l = SimpleLand(5, 5, 3, transit)
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
    l = Land1(10,10)
    im = ax.imshow(l.digitLand)
    im.figure.savefig("../output/Land1-Original.png")

    for i in range(generations):
        fileName = "../output/Land1-Gen-"+str(i+1)+".png"
        l = l.newGen()
        heat = ax.imshow(l.digitLand)
        heat.figure.savefig(fileName)

land1Test()