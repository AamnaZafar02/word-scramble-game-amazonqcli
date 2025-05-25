#!/usr/bin/env python3
import random

def scramble_word(word):
    """Scramble the letters of a word."""
    word_list = list(word)
    scrambled = word_list.copy()
    attempts = 0

    # Avoid infinite loop in case of words with same letters
    while ''.join(scrambled) == word and attempts < 10:
        random.shuffle(scrambled)
        attempts += 1

    return ''.join(scrambled)

def play_game():
    """Main game function."""
    words = [
        "python", "programming", "computer", "algorithm", "developer",
        "keyboard", "function", "variable", "database", "network",
        "software", "hardware", "internet", "security", "application"
    ]

    word = random.choice(words)
    scrambled = scramble_word(word)

    print("\n🔤 Welcome to Word Scramble!")
    print(f"🧩 Unscramble this word: {scrambled}")

    for attempt in range(3):
        tries_left = 2 - attempt
        guess = input(f"Attempt {attempt + 1}/3 ➤ Your guess: ").strip().lower()

        if guess == word:
            print(f"✅ Correct! The word was '{word}'.")
            print(f"🏆 You got it in {attempt + 1} {'try' if attempt == 0 else 'tries'}!")
            return True
        else:
            if tries_left > 0:
                print(f"❌ Wrong. You have {tries_left} {'try' if tries_left == 1 else 'tries'} left.")
            else:
                print(f"🚫 Out of attempts! The correct word was '{word}'.")
    return False

if __name__ == "__main__":
    score = 0
    rounds = 0

    while True:
        result = play_game()
        rounds += 1
        if result:
            score += 1

        print(f"\n📊 Score: {score}/{rounds}")
        play_again = input("🔁 Would you like to play again? (yes/no): ").strip().lower()

        if play_again not in ("yes", "y"):
            print("🎉 Thanks for playing! Goodbye!")
            break
