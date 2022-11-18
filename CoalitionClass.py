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