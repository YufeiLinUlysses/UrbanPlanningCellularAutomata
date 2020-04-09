import numpy as np
import random


class Land:
    n = 0
    row = 0
    col = 0
    land = np.matrix([1])
    transM = np.matrix([1])

    _total = row*col
    _natureCoverage = 0.25
    _residentialCoverageLower = 0.25
    _residentialCoverageUpper = 0.43
    _stochastic = []

    def __init__(self, r, c, n, matrix, land=None):
        if(r != 0 or c != 0):
            self.row = r
            self.col = c
            self.n = n
            self.transM = matrix
            if (land is not None):
                self.land = land
            else:
                self.land = np.matrix([[random.randint(0, n-1)
                                        for i in range(c)]for j in range(r)])
            self._total = r*c
            self._stochastic = np.matrix(
                [random.random() for i in range(self._total)])
        else:
            print("Please fix the input")

    def withTransitionMatrix(self):
        # Initialize a numpy array
        newLand = np.zeros(self._total, dtype=int)
        # Convert original land use to vector
        toVec = self.land.flatten('F')
        # Get a converted matrix from the vector form
        # Get boundaries
        conversion = np.zeros((self.n, self._total), dtype=int)
        for i in range(self._total):
            conversion[toVec.item(i)][i] = 1
        boundaries = self.transM.dot(conversion).transpose()
        # Get the new land
        for i in range(self._total):
            curT = -1
            prob = self._stochastic.item(i)
            for j in range(self.n):
                temp = self.n - j-1
                tProb = np.sort(boundaries[0]).item(temp)
                if (prob > tProb):
                    prob = prob-tProb
                    curT = np.argsort(boundaries[0]).item(temp-1)
                else:
                    curT = np.argsort(boundaries[0]).item(temp)
                    break
            newLand[i] = curT
        newLand = np.reshape(newLand, (self.row, self.col))
        nL =Land(self.row, self.col, self.n, self.transM, newLand)
        return nL
