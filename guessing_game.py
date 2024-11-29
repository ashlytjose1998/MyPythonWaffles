import random

import streamlit as st
import matplotlib.pyplot as plt
import openai
import random


openai.api_key = ":OPENAI_API_KEY"

if 'games_played' not in st.session_state:
    st.session_state['games_played'] = 0
if 'total_guesses' not in st.session_state:
    st.session_state['total_guesses'] = 0
if 'guess_history' not in st.session_state:
    st.session_state['guess_history'] = []


def ai_guessing_game():
    st.session_state.guesses = 0
    st.session_state.target = random.choice(["dog", "cat", "elephant", "tiger", "giraffe"])
    st.session_state.hints = []

    st.chat_message("assistant").markdown("Welcome to the guessing game! Try to guess the correct animal.")
    st.chat_message("assistant").markdown("I will give you hints after each guess. Let's start!")

    unique_key = f"guess_input_{st.session_state.guesses}"

    while True:
        user_guess = st.text_input("Your guess:", key=unique_key)
        if user_guess:
            st.session_state.guesses += 1
            if user_guess.lower() == st.session_state.target:
                st.chat_message("assistant").markdown("Congratulations! You've guessed the animal.")
                break
            else:
                # Providing a hint
                hint = get_hint(user_guess)
                st.chat_message("assistant").markdown(f"Hint: {get_hint(user_guess)}")
        st.session_state.guesses += 1

    st.session_state.append(st.session_state.guesses)
    return st.session_state.guesses


# OpenAI API call for generating hints
def get_hint(user_guess):
    prompt = f"Is the animal I am thinking of a {user_guess}? Please provide a hint for the user."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()


# Main function for displaying the pages
def main():
    st.set_page_config(page_title="Guessing Game", layout="wide")

    # Navigation between pages
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", ["Play", "Stats"])

    if page == "Play":
        st.title("Guess the Animal Game")
        if "guesses" not in st.session_state:
            st.session_state.guesses = 0
        if "target" not in st.session_state:
            st.session_state.target = ""
        if "hints" not in st.session_state:
            st.session_state.hints = []

        # Start a new game
        if st.button("Start New Game"):
            ai_guessing_game()

    elif page == "Stats":
        st.title("Game Statistics")

        # Displaying stats
        st.write(f"Number of games played: {st.session_state['games_played']}")
        if st.session_state['games_played'] > 0:
            avg_guesses = ['guess_history'] / ['games_played']
            st.write(f"Average number of guesses per game: {avg_guesses:.2f}")

        # Displaying bar chart for guesses per game
        if ['guess_history']:
            fig, ax = plt.subplots()
            ax.bar(range(1, len(['guess_history']) + 1), ['guess_history'])
            ax.set_xlabel('Game Number')
            ax.set_ylabel('Guesses per Game')
            ax.set_title('Guesses per Game')
            st.pyplot(fig)


# Run the app
if __name__ == "__main__":
    main()
