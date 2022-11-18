from CoalitionClass import *

def getWinningCoalitions(quota, weighted_votes):
    "returns an instance of CoalitionClass"
    nvoters = len(weighted_votes)
    coalitionList = CoalitionList()
    for subset in range(1, 2**nvoters):
        cur_coalition = Coalition(weighted_votes, quota)
        for voter_index in range(nvoters):
            if subset & (1 << voter_index):
                cur_coalition.addVoter(voter_index)
        
        cur_coalition.ProcessCoalition()
        coalitionList.addCoalition(cur_coalition)
        
    return coalitionList


def main(quota, weighted_votes):
    coalitionList = getWinningCoalitions(quota, weighted_votes)
    # create voter class

main(int(input()), [int(i) for i in input().split()])
