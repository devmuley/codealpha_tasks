import random

WORDS = ["python", "guitar", "jungle", "rocket", "laptop"]

def get_display(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)

def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0
    max_wrong = 6

    print("=" * 30)
    print("      HANGMAN GAME")
    print("=" * 30)

    while wrong < max_wrong:

        print("\nWord:", get_display(word, guessed))

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed:
            print(f"You already guessed '{guess}'.")
            continue

        guessed.append(guess)

        if guess in word:
            print(f"'{guess}' is in the word!")
        else:
            wrong += 1
            print(f"Wrong! {wrong}/{max_wrong} incorrect guesses.")

        print("Guessed:", ", ".join(sorted(guessed)))

        display = get_display(word, guessed)

        if "_" not in display:
            print(f"\nCongratulations! You guessed: {get_display(word, guessed)}")
            print(f"The word was: {word}")
            return

    print(f"\nOut of chances! The word was '{word}'.")

while True:
    play()
    again = input("\nPlay again? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Thanks for playing!")
        break