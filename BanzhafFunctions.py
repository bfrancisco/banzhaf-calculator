from CoalitionClass import *

def getCoalitions(quota, weighted_votes):
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

def getVoterStats(quota, weighted_votes, coalitionList):
    "Process banzhaf powers and power indeces of all voters. "
    nvoters = len(weighted_votes)
    voterList = [Voter() for v in range(nvoters)]
    
    # calculate banzhaf powers
    for coalition in coalitionList.coalitionList:
        for voter_index in range(nvoters):
            if coalition.isWin and voter_index in coalition.voter_indeces_set:
                if coalition.total_votes - weighted_votes[voter_index] < quota:
                    voterList[voter_index].incrementBanzhafPower()
                    voterList[voter_index].addWinningCoalition(coalition)
    
    # calculate banzhaf power indeces
    sumBanzhafPower = 0
    for voter_index in range(nvoters):
        sumBanzhafPower += voterList[voter_index].getBanzhafPower()
    for voter_index in range(nvoters):
        voterList[voter_index].calculatePowerIndex(sumBanzhafPower)

    return voterList

        

def ProcessBanzhaf(quota, weighted_votes):
    coalitionList = getCoalitions(quota, weighted_votes)
    voterList = getVoterStats(quota, weighted_votes, coalitionList)

    # print check
    # for i in range(len(weighted_votes)):
    #     print(i+1, ":", voterList[i].getPowerIndex())

    return coalitionList, voterList

#main(int(input()), [int(i) for i in input().split()])
