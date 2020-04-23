from land import Land
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def landTest():
    # Initialize plot
    fig, ax = plt.subplots()

    # Look at the change over a period of time
    generations = 10

    # Initialize a land
    l = Land(10, 10)
    im = ax.imshow(l.digitLand)
    im.figure.savefig("../output/Land2/Land2-Gen-0.png")

    for i in range(generations):
        fileName = "../output/Land2/Land2-Gen-"+str(i+1)+".png"
        l = l.newGen()
        heat = ax.imshow(l.digitLand)
        heat.figure.savefig(fileName)


landTest()
