import streamlit as st 
import random
from monty_hall import simulate_game

import time

st.image('./src/images/banner.png')

num_games = st.number_input("Enter the number of game to simulate", min_value=1, max_value=1000000)

wins_no_switch = 0
wins_switch = 0

col1, col2 = st.columns(2)
col1.subheader("Wins percentage without switching")
chart1 = col1.line_chart(x=None, y=None, width=0, height=400)
col2.subheader("Wins percentage with switching")
chart2 = col2.line_chart(x=None, y=None, width=0, height=400)

for i in range(num_games):

    num_wins_without_switching, num_wins_with_switching = simulate_game(1)

    wins_no_switch += num_wins_without_switching
    wins_switch += num_wins_with_switching


    chart1.add_rows([wins_no_switch / (i+1)])
    chart2.add_rows([wins_switch / (i+1)])



time.sleep(0.01)