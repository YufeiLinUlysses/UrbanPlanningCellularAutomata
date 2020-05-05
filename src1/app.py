from land import Land
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def landTest():
    # Sustainability Result
    result = ""

    # Initialize plot
    fig, ax = plt.subplots()

    # Look at the change over a period of time
    generations = 10

    # Initialize a land
    l = Land(10, 10)
    result += l.sustanabilityAssessment(0)+"\n"
    im = ax.imshow(l.digitLand)
    im.figure.savefig("../output/Land3/Land3-Gen-0.png")
    
    for i in range(generations):
        fileName = "../output/Land3/Land3-Gen-"+str(i+1)+".png"
        l = l.newGen()
        result += l.sustanabilityAssessment(i+1)+"\n"
        heat = ax.imshow(l.digitLand)
        heat.figure.savefig(fileName)
        
    f = open("../output/Land3/Sustainability Assessment.txt", "w")
    f.write(result)
    f.close()


landTest()
