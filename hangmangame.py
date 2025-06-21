import random

def play_hangman():
    words = ['python', 'hangman', 'script', 'input', 'project']
    word_to_guess = random.choice(words)

    guessed_letters = []
    attempts = 6
    display_word = ['_'] * len(word_to_guess)

    print("\n Welcome to Hangman!")

    while attempts > 0 and '_' in display_word:
        print("\nWord:", ' '.join(display_word))
        print("Guessed letters:", guessed_letters)
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(" Please enter a single alphabet only.")
            continue

        if guess in guessed_letters:
            print(" You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    display_word[i] = guess
            print(" Correct guess!")
        else:
            attempts -= 1
            print(" Wrong guess. Attempts left:", attempts)

    if '_' not in display_word:
        print("\n Congratulations! You guessed the word:", word_to_guess)
    else:
        print("\n Game Over! The correct word was:", word_to_guess)

while True:
    play_hangman()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print(" Thanks for playing Hangman! See you next time.")
        break
