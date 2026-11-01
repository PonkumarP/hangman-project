# Hangman Game - Python Console Application

## 📋 Project Overview

A simple, beginner-friendly **Hangman Game** built with **Python** for the **CodeAlpha Python Programming Internship**. This console-based word guessing game challenges players to guess a secret word letter by letter before running out of attempts.

---

## 🎮 Game Features

✅ **5 Predefined Words** - Randomly selects from a list of English words  
✅ **6 Maximum Attempts** - Players get 6 chances to make wrong guesses  
✅ **Letter Validation** - Accepts only single alphabetic characters  
✅ **Duplicate Prevention** - Warns users if they guess the same letter twice (no penalty)  
✅ **Visual Hangman Display** - ASCII art shows game progress  
✅ **Clear Feedback** - Shows correctly guessed letters, wrong guesses, and remaining attempts  
✅ **Win/Loss Messages** - Congratulates winners and reveals the word to losers  
✅ **Play Again Option** - Allows multiple rounds without restarting the program  

---

## 🛠️ Technical Requirements

### Language & Modules
- **Python 3.x** (Python 3.6 or higher recommended)
- **Built-in modules used:**
  - `random` - For random word selection
  - No external libraries required!

### Concepts Demonstrated
- Functions
- Lists and Sets
- Loops (while, for)
- Conditionals (if-elif-else)
- String manipulation
- Input validation
- Random selection

---

## 📦 Installation & Setup

### Prerequisites
Make sure you have Python installed on your system.

**Check Python version:**
```bash
python --version
```
or
```bash
python3 --version
```

### Download the Project
1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_HangmanGame.git
cd CodeAlpha_HangmanGame
```

Or download the `hangman.py` file directly.

---

## 🚀 How to Run the Game

### Method 1: Using Terminal/Command Prompt

**On macOS/Linux:**
```bash
python3 hangman.py
```

**On Windows:**
```bash
python hangman.py
```

### Method 2: Using an IDE
1. Open `hangman.py` in your favorite IDE (VS Code, PyCharm, IDLE, etc.)
2. Click the **Run** button or press **F5**

---

## 🎯 How to Play

1. **Start the game** - Run the program to see the welcome screen
2. **View the word** - The secret word appears as underscores: `_ _ _ _ _`
3. **Guess letters** - Type one letter at a time and press Enter
4. **Track progress:**
   - ✅ Correct guesses reveal letters in the word
   - ❌ Wrong guesses reduce your remaining attempts
5. **Win condition** - Guess all letters before attempts run out
6. **Lose condition** - Run out of attempts (6 wrong guesses)
7. **Play again** - Choose 'yes' to play another round or 'no' to exit

---

## 📸 Sample Terminal Output

```
==================================================
Welcome to HANGMAN GAME!
==================================================
Rules:
- Guess one letter at a time
- You have 6 incorrect attempts
- Guess the word before attempts run out!
==================================================

==================================================

           --------
           |      |
           |      
           |    
           |      
           |     
           -
        
==================================================

Word: _ _ _ _ _ _
Attempts remaining: 6/6
Guessed letters: None
Wrong guesses: None
Enter a letter: p

✅ Good guess! 'P' is in the word!

==================================================

           --------
           |      |
           |      
           |    
           |      
           |     
           -
        
==================================================

Word: P _ _ _ _ _
Attempts remaining: 6/6
Guessed letters: P
Wrong guesses: None
Enter a letter: y

✅ Good guess! 'Y' is in the word!

==================================================

           --------
           |      |
           |      
           |    
           |      
           |     
           -
        
==================================================

Word: P Y _ _ _ _
Attempts remaining: 6/6
Guessed letters: P, Y
Wrong guesses: None
Enter a letter: z

❌ Sorry! 'Z' is not in the word.
Remaining attempts: 5

...

==================================================
🎉 CONGRATULATIONS! You won! 🎉
The word was: PYTHON
==================================================

Do you want to play again? (yes/no): no

==================================================
Thank you for playing Hangman!
Made for CodeAlpha Python Programming Internship
==================================================
```

---

## 📂 Project Structure

```
CodeAlpha_HangmanGame/
│
├── hangman.py          # Main game source code
└── README.md           # Project documentation (this file)
```

---

## 🔧 Code Explanation (Step by Step)

### **Step 1: Import Required Module**
```python
import random
```
- We use the `random` module to randomly select a word from our list.

### **Step 2: Display Welcome Message**
```python
def display_welcome():
```
- Shows game title, rules, and instructions when the game starts.

### **Step 3: Get Random Word**
```python
def get_random_word():
    word_list = ["python", "coding", "computer", "hangman", "programming"]
    return random.choice(word_list).upper()
```
- Creates a list of 5 words
- Uses `random.choice()` to pick one randomly
- Converts to uppercase for consistency

### **Step 4: Display Word with Underscores**
```python
def display_word(word, guessed_letters):
```
- Shows correctly guessed letters in their positions
- Shows underscores `_` for unguessed letters

### **Step 5: Display Hangman Visual**
```python
def display_hangman(attempts_left):
```
- Shows ASCII art of hangman stages
- Updates based on remaining attempts (0-6)

### **Step 6: Get Valid Guess**
```python
def get_valid_guess(guessed_letters):
```
- Gets user input
- Validates:
  - Only single character
  - Only alphabetic letters
  - Not previously guessed
- Loops until valid input is received

### **Step 7: Main Game Logic**
```python
def play_hangman():
```
- Initializes game variables
- Runs the game loop:
  - Displays current state
  - Gets user guess
  - Checks if guess is correct
  - Updates attempts
  - Checks win/loss conditions

### **Step 8: Play Again Function**
```python
def play_again():
```
- Asks if player wants another round
- Validates yes/no response

### **Step 9: Main Function**
```python
def main():
```
- Entry point of the program
- Displays welcome message
- Runs game loop until player quits

### **Step 10: Run the Game**
```python
if __name__ == "__main__":
    main()
```
- Ensures the game runs only when executed directly
- Not when imported as a module

---

## 🌟 Key Programming Concepts Used

| Concept | Usage in Project |
|---------|------------------|
| **Functions** | Modular code organization (`display_welcome`, `play_hangman`, etc.) |
| **Lists** | Storing word list |
| **Sets** | Tracking guessed letters (no duplicates) |
| **Loops** | `while` loop for game rounds, `for` loop for word display |
| **Conditionals** | `if-elif-else` for game logic and validation |
| **String Methods** | `.upper()`, `.isalpha()`, `.lower()` |
| **Input Validation** | Checking single character, alphabetic input |
| **Random Module** | `random.choice()` for word selection |

---

## 📤 How to Upload to GitHub

### Step 1: Create a Repository
1. Go to [GitHub](https://github.com)
2. Click **"New Repository"**
3. Name it: **CodeAlpha_HangmanGame**
4. Add description: "Hangman Game - Python Console Application for CodeAlpha Internship"
5. Keep it **Public**
6. Click **"Create Repository"**

### Step 2: Upload Files via GitHub Web Interface (Easy Method)
1. Click **"uploading an existing file"**
2. Drag and drop `hangman.py` and `README.md`
3. Click **"Commit changes"**

### Step 3: Upload via Git (Command Line Method)
```bash
# Navigate to your project folder
cd /Users/ponkumar/Desktop/On\ Intern/1

# Initialize Git repository
git init

# Add files
git add hangman.py README.md

# Commit changes
git commit -m "Initial commit: Hangman Game for CodeAlpha Internship"

# Add remote repository (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/CodeAlpha_HangmanGame.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## 🎓 Learning Outcomes

By completing this project, you have demonstrated:
- ✅ Python fundamentals (variables, functions, loops, conditionals)
- ✅ Working with built-in modules (`random`)
- ✅ Input validation and error handling
- ✅ String manipulation and data structures (lists, sets)
- ✅ Code organization and documentation
- ✅ Git and GitHub version control

---

## 🐛 Troubleshooting

### Issue: "python: command not found"
**Solution:** Try `python3` instead of `python`

### Issue: Game not displaying properly
**Solution:** Ensure your terminal supports UTF-8 encoding

### Issue: Special characters not showing (✅, ❌, 🎉)
**Solution:** These are optional emoji. The game will still work without them.

---

## 👨‍💻 Author

**Project Created for:** CodeAlpha Python Programming Internship  
**Developer:** [Your Name]  
**Date:** [Current Date]  

---

## 📜 License

This project is created for educational purposes as part of the CodeAlpha internship program.

---

## 🙏 Acknowledgments

- **CodeAlpha** - For providing this internship opportunity
- **Python Community** - For excellent documentation and resources

---

## 📞 Contact

For any questions or feedback, feel free to reach out!

**GitHub:** [Your GitHub Profile]  
**Email:** [Your Email]

---

**Happy Coding! 🐍✨**
