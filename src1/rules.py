import numpy as np
import random
# This is the rule for a cell has neighbours of one particular type


class Rule:
    probs = None

    def __init__(self, ruleMatrix):
        self.probs = np.matrix(ruleMatrix)


def AllNature():
    rule = Rule([
        [0.6, 0.1, 0.15, 0.15],
        [0.05, 0.8, 0.1, 0.05],
        [0.05, 0.15, 0.7, 0.1],
        [0.08, 0.02, 0.1, 0.8]
    ])
    return rule


def AllResidential():
    rule = Rule([
        [0.84, 0.05, 0.06, 0.05],
        [0.03, 0.52, 0.39, 0.06],
        [0.01, 0.20, 0.61, 0.18],
        [0.2, 0.02, 0.18, 0.6]
    ])
    return rule


def AllCommercial():
    rule = Rule([
        [0.5, 0.12, 0.3, 0.08],
        [0.02, 0.8, 0.1, 0.08],
        [0.04, 0.18, 0.6, 0.18],
        [0.19, 0.04, 0.26, 0.51]
    ])
    return rule


def AllIndustrial():
    rule = Rule([
        [0.45, 0.01, 0.18, 0.36],
        [0.2, 0.5, 0.1, 0.2],
        [0.25, 0.02, 0.45, 0.28],
        [0.04, 0, 0.16, 0.8]
    ])
    return rule
