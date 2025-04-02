
# Password Generator

A simple Python script that generates a secure, random password based on user preferences for letters, symbols, and numbers.

## Features
- **Customizable Length**: Choose how many letters, symbols, and numbers your password contains.
- **Secure Randomization**: Uses Python's `random` module to shuffle characters.
- **Flexible Character Sets**: Includes:
  - Uppercase and lowercase letters (`A-Z, a-z`)
  - Common symbols (`!@#$%^&*`, etc.)
  - Numbers (`0-9`)

## How to Use
1. **Run the script** in a Python environment (Python 3.6+ recommended):
   ```bash
   python password_generator.py
   ```
2. **Follow the prompts** to specify the number of letters, symbols, and numbers.
3. **Copy your generated password** from the output.

### Example Output:
```
Let's generate a random password for you
How many letters should the password have? 8
How many symbols should the password have? 2
How many numbers should the password have? 2
Your password is: pA5!k9Lz@
```

## Code Overview
- **Character Sets**: Predefined lists for letters, symbols, and numbers.
- **User Input**: Dynamically accepts desired character counts.
- **Randomization**: Combines and shuffles characters for security.

## Requirements
- Python 3.x

## Customization
Modify the `letters`, `symbols`, or `numbers` lists in the script to change the allowed characters.
