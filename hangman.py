import random

def display_welcome():
    print("\n" + "="*50)
    print("Welcome to HANGMAN GAME!")
    print("="*50)
    print("Rules:")
    print("- Guess one letter at a time")
    print("- You have 6 incorrect attempts")
    print("- Guess the word before attempts run out!")
    print("="*50 + "\n")

def get_random_word():
    word_list = ["python", "coding", "computer", "hangman", "programming"]
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def display_hangman(attempts_left):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[attempts_left]

def get_valid_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").upper()
        
        if len(guess) != 1:
            print("❌ Please enter only ONE letter!")
            continue
        
        if not guess.isalpha():
            print("❌ Please enter only ALPHABETIC characters!")
            continue
        
        if guess in guessed_letters:
            print(f"❌ You already guessed '{guess}'. Try a different letter!")
            continue
        
        return guess

def play_hangman():
    word = get_random_word()
    
    max_attempts = 6
    attempts_left = max_attempts
    guessed_letters = set()
    wrong_guesses = set()
    
    while attempts_left > 0:
        print("\n" + "="*50)
        print(display_hangman(attempts_left))
        print("="*50)
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts_left}/{max_attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Wrong guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'}")
        
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word!")
            
            if all(letter in guessed_letters for letter in word):
                print("\n" + "="*50)
                print(f"🎉 CONGRATULATIONS! You won! 🎉")
                print(f"The word was: {word}")
                print("="*50)
                return True
        else:
            print(f"❌ Sorry! '{guess}' is not in the word.")
            wrong_guesses.add(guess)
            attempts_left -= 1
            print(f"Remaining attempts: {attempts_left}")
    
    print("\n" + "="*50)
    print(display_hangman(0))
    print("="*50)
    print(f"😢 GAME OVER! You ran out of attempts!")
    print(f"The correct word was: {word}")
    print("="*50)
    return False

def play_again():
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'")

def main():
    display_welcome()
    
    while True:
        play_hangman()
        
        if not play_again():
            print("\n" + "="*50)
            print("Thank you for playing Hangman!")
            print("Made for CodeAlpha Python Programming Internship")
            print("="*50 + "\n")
            break

if __name__ == "__main__":
    main()
