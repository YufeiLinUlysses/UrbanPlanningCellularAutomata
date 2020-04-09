from land import Land
import numpy as np

#Look at the change over a period of time
generations = 10

#Transition Matrix
transit = np.matrix([
    [0.7, 0.4, 0.5],
    [0.2, 0.4, 0.3],
    [0.1, 0.2, 0.2]
])

#Initialize a land
l = Land(3, 2, 3, transit)
print(l.land)

for i in range (generations):
    l = l.withTransitionMatrix()
    print(l.land)
