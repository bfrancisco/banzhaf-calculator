class Coalition:
    def __init__(self, voter_indeces, isWin, hasVeto):
        self.voter_indeces = voter_indeces
        self.isWin = isWin
        self.hasVeto = hasVeto
        self.voter_indeces_set = set(voter_indeces)
    
    def isWinning(self):
        return self.isWin
    
    def hasVetoPower(self):
        return self.hasVeto
    
    def getVoterIndeces(self):
        return self.voter_indeces

    def addVoter(self, voter_index):
        self.voter_indeces.append(voter_index)
        self.voter_indeces_set.add(voter_index)


def getWinningCoalitions(quota, weighted_votes):

    nvoters = len(weighted_votes)
    win_coalitions = []
    for subset in range(1, 2**nvoters):
        print(bin(subset)[2:])
        subset1 = []
        subset0 = []
        for i in range(nvoters):
            if subset & (1 << i):
                subset1.append(i)
            else:
                subset0.append(i)
        


def main(quota, weighted_votes):
    winning_coalitions = getWinningCoalitions(quota, weighted_votes)


main(int(input()), [int(i) for i in input().split()])