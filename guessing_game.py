import streamlit as st
import random
import openai
import matplotlib.pyplot as plt
import numpy as np

openai.api_key = ':OPENAI_API_KEY'

game_count = 0
total_guesses = 0
guesses_per_game = []


def ai_guessing_game():
    st.session_state.guesses = 0
    # The question could be dynamically generated or fixed for now (for example: guessing an animal)
    st.session_state.target = random.choice(["dog", "cat", "elephant", "tiger", "giraffe"])
    st.session_state.hints = []

    st.chat_message("assistant").markdown("Welcome to the guessing game! Try to guess the correct animal.")
    st.chat_message("assistant").markdown("I will give you hints after each guess. Let's start!")

    while True:
        user_guess = st.text_input("Your guess:", key="guess_input")
        if user_guess:
            st.session_state.guesses += 1
            if user_guess.lower() == st.session_state.target:
                st.chat_message("assistant").markdown("Congratulations! You've guessed the animal.")
                break
            else:
                # Providing a hint using a simple AI prompt for natural language processing
                hint = get_hint(user_guess)
                st.chat_message("assistant").markdown(f"Hint: {hint}")
        st.session_state.guesses += 1

    guesses_per_game.append(st.session_state.guesses)
    return st.session_state.guesses


# OpenAI API call for generating hints or evaluating guesses
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
        st.write(f"Number of games played: {game_count}")
        if game_count > 0:
            avg_guesses = total_guesses / game_count
            st.write(f"Average number of guesses per game: {avg_guesses:.2f}")

        # Displaying bar chart for guesses per game
        if guesses_per_game:
            fig, ax = plt.subplots()
            ax.bar(range(1, len(guesses_per_game) + 1), guesses_per_game)
            ax.set_xlabel('Game Number')
            ax.set_ylabel('Guesses per Game')
            ax.set_title('Guesses per Game')
            st.pyplot(fig)


# Run the app
if __name__ == "__main__":
    main()