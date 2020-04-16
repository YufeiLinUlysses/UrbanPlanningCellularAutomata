class Rule:
    # rule we would like to have, usually in a lambda function
    rule = True
    # array of probabilities each index represnets a land use type
    probs = []

    def __init__(self, probs, rule=None):
        if rule is None:
            self.rule = lambda cell: True
        else:
            self.rule = rule
        self.probs = probs
