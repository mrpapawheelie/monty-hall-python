import streamlit as st
import random

def monty_hall_simulation(num_trials):
    stick_wins, switch_wins = 0, 0

    for _ in range(num_trials):
        car_position, contestant_choice = random.randint(1, 3), random.randint(1, 3)
        door_opened_by_host = next(door for door in [1, 2, 3] if door != contestant_choice and door != car_position)
        remaining_door = next(door for door in [1, 2, 3] if door != contestant_choice and door != door_opened_by_host)

        stick_wins += contestant_choice == car_position
        switch_wins += remaining_door == car_position

    return stick_wins, switch_wins

def monty_hall():
    st.set_page_config(page_title="Monty Hall Simulation", page_icon="🎲")
    st.title("Monty Hall Problem Simulator")
    # Explanation and Instructions
    st.write("""
    
    ### What is the Monty Hall Problem?
    The Monty Hall problem is a famous statistical puzzle. Imagine you're on a game show and presented with three doors. Behind one door is a car (the prize), and behind the other two doors are goats. You choose a door, and then the host, who knows what's behind the doors, opens another door, revealing a goat. You're then given a choice: stick with your original pick or switch to the remaining unopened door. What's your best strategy?

    ### Purpose of This Simulation
    This simulation allows you to run multiple trials of the Monty Hall problem to see statistically whether you're better off sticking with your original choice or switching doors. Try adjust the sample size to a small number to see the difference.

    ### How to Use This Simulator
    1. Enter the number of trials in the input box.
    2. Click the 'Run Simulation' button to start the simulation.
    3. The results will show how often sticking or switching would have won.
    4. Use these results to understand the probabilities involved in the Monty Hall problem.
    """)

    num_trials = st.number_input('Enter the number of trials', min_value=1, value=1000)

    if st.button('Run Simulation'):
        stick_wins, switch_wins = monty_hall_simulation(num_trials)
        stick_percentage = stick_wins / num_trials * 100
        switch_percentage = switch_wins / num_trials * 100

        st.write(f"Sticking with the original choice won {stick_wins} times out of {num_trials} ({stick_percentage:.2f}%)")
        st.write(f"Switching to the other door won {switch_wins} times out of {num_trials} ({switch_percentage:.2f}%)")

monty_hall()
