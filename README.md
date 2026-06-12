# 🎯 Hangman Game

A simple text-based Hangman game built using Python. The player guesses a hidden word one letter at a time before running out of chances.

## Features

* Random word selection from a predefined list
* Maximum of 6 incorrect guesses allowed
* Input validation for single alphabetic characters
* Prevents duplicate guesses
* Displays guessed letters
* Win and lose conditions
* Play Again option

## Technologies Used

* Python 3
* Random Module
* Functions
* Lists
* Loops
* Conditional Statements

## How to Run

1. Download or clone the repository.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python hangman.py
```

## How to Play

1. A random word is selected by the computer.
2. The word is displayed as underscores (_).
3. Enter one letter at a time.
4. Correct guesses reveal letters in the word.
5. Incorrect guesses reduce the remaining chances.
6. Guess the complete word before reaching 6 incorrect guesses.

## Sample Output

```text
==============================
      HANGMAN GAME
==============================

Word: _ _ _ _ _ _
Guess a letter: p

'p' is in the word!
Guessed: p

Word: p _ _ _ _ _
```

## Project Structure

```text
codealpha_tasks/
└── hangman.py
```

## Future Improvements

* Add ASCII Hangman graphics
* Add difficulty levels
* Load words from an external file
* Add categories of words
* Display remaining lives visually

## Author

Devarsh Muley
