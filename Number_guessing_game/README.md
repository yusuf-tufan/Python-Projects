# 🎯 Number Guessing Game (with Python & Tkinter)

A simple yet interactive Number Guessing Game built using **Python** and **Tkinter**. This game allows the player to define an upper limit for the number range, and then attempt to guess a randomly selected number within that range. Informative messages guide the player throughout the game, including error handling for invalid inputs.

---

## 🕹️ How It Works

1. **Set Range**: The player inputs a number to define the upper boundary of the guessing range (e.g., entering `100` sets the range from `0` to `100`).
2. **Start Guessing**: The game generates a random number within the defined range.
3. **Make Guesses**: The player attempts to guess the number, receiving feedback after each attempt:
   - 🔼 *"Too high!"*
   - 🔽 *"Too low!"*
   - ✅ *"Correct!"*
4. **Validation**: The game handles invalid inputs gracefully, such as non-numeric entries, empty fields, or guesses outside the allowed range.

---

## 💡 Features

- User-friendly **GUI** with Tkinter
- Customizable number range
- Dynamic feedback messages
- Error handling for:
  - Non-integer input
  - Empty input fields
  - Guesses outside the specified range
- Clean and responsive interface

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** (for GUI)
- **random** module (for number generation)

---