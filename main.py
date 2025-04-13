import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game")

st.title("Number Guessing Game")
st.write("Guess a number between 1 and 100!")

# Initialize session state variables
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Input from user
guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if st.session_state.game_over:
        st.warning("Game over! Click 'Restart' to play again.")
    else:
        st.session_state.attempts += 1
        if guess < st.session_state.number:
            st.info("Too low! Try again.")
        elif guess > st.session_state.number:
            st.info("Too high! Try again.")
        else:
            st.success(f"Correct! You guessed it in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True

# Restart the game
if st.button("Restart"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.experimental_rerun()
