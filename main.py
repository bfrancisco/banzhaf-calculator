import streamlit as st
import BanzhafFunctions

if __name__ == '__main__':

    st.set_page_config(
        page_title="Banzhaf Calculator"
    )

    st.title("Banzhaf Power Index Calculator")
    st.caption("© Copyright 2022 by James Bryan Francisco - ADMU BS CS")

    weighted_votes_string = st.text_input("Weighted Votes", placeholder = "10 15 12 7")
    weighted_votes = [int(i) for i in weighted_votes_string.split()]
    quota = st.number_input("Quota", min_value = 1, max_value = sum(weighted_votes))
    
    bttn = st.button("Calculate results")
    if bttn:
        coalitionList, voterList = BanzhafFunctions.ProcessBanzhaf(quota, weighted_votes)
        sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        st.subheader("List of Coalitions")
        srted_coalitionList = sorted(coalitionList.coalitionList)
        for coalition in srted_coalitionList:
            lst_coalition = []
            for index in coalition.voter_indeces:
                lst_coalition.append("V"+str(index+1))
            lst_coalition_string = " ".join(lst_coalition)
            lst_coalition_string = lst_coalition_string.translate(sub)
            
            out = "(" + lst_coalition_string + ")" + " "
            if coalition.isWin:
                out += "is Winning and "
            else:
                out += "is Losing and "
            if coalition.hasVeto:
                out += "has Veto Power"
            else:
                out += "doesn't have Veto Power"
            st.write(out)
        
        for i in range(len(weighted_votes)):
            st.subheader("Voter " + str(i+1))
            st.write("Weight of vote:", weighted_votes[i])
            st.write("Banzhaf Power Index:", voterList[i].getPowerIndex())
            st.write("Banzhaf Power:", voterList[i].getBanzhafPower())

            if voterList[i].isCritical():
                if voterList[i].isDictator():
                    st.write("Voter", i+1, "is a dictator.")
                else:
                    st.write("Voter", i+1, "is a critical voter.")
                winning_coalitions_strings = []
                for win_coalition in voterList[i].getWinningCoalitions():
                    voter_indeces_string = '( '
                    for index in win_coalition.voter_indeces:
                        
                        voter_indeces_string += 'V' + str(index+1) + ', '
                    
                    voter_indeces_string = voter_indeces_string[:-2] + ' )'
                    voter_indeces_string = voter_indeces_string.translate(sub)
                    winning_coalitions_strings.append(voter_indeces_string)

                coalitions_out = ""
                for coalition in winning_coalitions_strings:
                    coalitions_out += coalition + ', '

                st.write("Critical Coalitions:", coalitions_out[:-2])
                
            elif voterList[i].isDummy():
                st.write("Voter", i+1, "is a dummy voter.")
        

        