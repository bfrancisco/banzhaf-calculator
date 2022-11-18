import streamlit as st
import BanzhafFunctions

if __name__ == '__main__':

    st.set_page_config(
        page_title="Banzhaf Calculator"
    )

    st.title("Banzhaf Power Index Calculator")
    st.caption("© Copyright 2022 by James Bryan Francisco - ADMU BS CS")

    quota = st.number_input("Quota", min_value = 1)
    weighted_votes_string = st.text_input("Weighted votes", placeholder = "10 15 12 7")
    weighted_votes = [int(i) for i in weighted_votes_string.split()]

    coalitionList, voterList = BanzhafFunctions.ProcessBanzhaf(quota, weighted_votes)

    for i in range(len(weighted_votes)):
        st.write("Voter", i+1, ":", voterList[i].getPowerIndex())
