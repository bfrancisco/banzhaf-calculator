from CoalitionClass import Coalition

def getWinningCoalitions(quota, weighted_votes):
    nvoters = len(weighted_votes)
    win_coalitions = []
    for subset in range(1, 2**nvoters):
        cur_coalition = Coalition(weighted_votes, quota)
        for voter_index in range(nvoters):
            if subset & (1 << voter_index):
                cur_coalition.addVoter(voter_index)
        
        cur_coalition.ProcessCoalition()

        if cur_coalition.isWin:
            win_coalitions.append(cur_coalition)
        
    return win_coalitions


def main(quota, weighted_votes):
    winning_coalitions = getWinningCoalitions(quota, weighted_votes)
    for c in winning_coalitions:
        print(c.voter_indeces)

main(int(input()), [int(i) for i in input().split()])
