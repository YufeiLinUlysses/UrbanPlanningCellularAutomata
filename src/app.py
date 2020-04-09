from land import Land
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Initialize plot
fig, ax = plt.subplots()

# Look at the change over a period of time
generations = 10

# Transition Matrix
transit = np.matrix([
    [0.7, 0.4, 0.5],
    [0.2, 0.4, 0.3],
    [0.1, 0.2, 0.2]
])

# Initialize a land
l = Land(5, 5, 3, transit)
im = ax.imshow(l.land)
im.figure.savefig("../output/Original.png")

for i in range(generations):
    fileName = "../output/Gen-"+str(i+1)+".png"
    l = l.withTransitionMatrix()
    heat = ax.imshow(l.land)
    heat.figure.savefig(fileName)

