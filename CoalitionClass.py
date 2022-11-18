class Coalition:
    def __init__(self, weighted_votes, quota):
        self.weighted_votes = weighted_votes
        self.nvoters = len(self.weighted_votes)
        self.voter_indeces = []
        self.voter_indeces_set = set(self.voter_indeces)
        self.quota = quota

        self.complete_data = False
        self.total_votes = 0
        self.complement_votes = 0
        self.isWin = False 
        self.hasVeto = False
    
    def ProcessCoalition(self):
        for index in range(self.nvoters):
            if index in self.voter_indeces_set:
                self.total_votes += self.weighted_votes[index]
            else:
                self.complement_votes += self.weighted_votes[index]
        
        if self.total_votes >= self.quota:
            self.isWin = True
        
        if self.complement_votes < self.quota:
            self.hasVeto = True
        
        self.complete_data = True

    def addVoter(self, voter_index):
        self.voter_indeces.append(voter_index)
        self.voter_indeces_set.add(voter_index)

class CoalitionList:
    def __init__(self):
        self.coalitionList = []
        self.hasVetoSet = set() 
        self.isWinningSet = set()
    
    def addCoalition(self, coalition):

        self.coalitionList.append(coalition.voter_indeces)
        if coalition.hasVeto:
            self.hasVetoSet.add(coalition.voter_indeces)
        if coalition.isWin:
            self.isWinningSet.add(coalition.voter_indeces)
    
    def isCoalitionHasVeto(self, voter_indeces_1indexed):
        voter_indeces_0indexed = [i-1 for i in voter_indeces_1indexed]
        voter_indeces_0indexed.sort()
        if voter_indeces_0indexed in self.hasVetoSet:
            return True
        return False

    def isCoalitionWinning(self, voter_indeces_1indexed):
        voter_indeces_0indexed = [i-1 for i in voter_indeces_1indexed]
        voter_indeces_0indexed.sort()
        if voter_indeces_0indexed in self.isWinningSet:
            return True
        return False