from game_logic.hint_generator import provide_hint
from game_logic.number_generator import generate_random_number
from game_logic.scorer import Scorer
from utils.input_validation import get_valid_input


def main():
    number_to_guess = generate_random_number(1, 100)
    score = Scorer()

    while True:
        guess = get_valid_input("Enter your guess between 1 and 100: ", 1, 100)

        if guess == number_to_guess:
            print(f"Congratulations! Your final score is {score.get_score()} ")

            break

        else:
            hint = provide_hint(guess, number_to_guess)
            print(hint)
            score.decrement_score()


if __name__ == "__main__":
    main()