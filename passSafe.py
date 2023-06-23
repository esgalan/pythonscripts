#!/usr/bin/python3

import string
import secrets

# Prompt user to determine action
choice = input("Welcome to Pass-Safe v1.0\n\nWould you like to generate a password?(y/n): ")

# Logic to generate random password
if choice == "y":
    # Defining the scope for password generation
    alphabet = string.ascii_letters + string.digits
    # Logic to generate random password
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(16))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
                break
    # Inserting '-' character after every fourth character in the password string
    password = '-'.join(password[i:i+4] for i in range(0, len(password), 4))
    c
else:
    print("Very well... Thank you for considering Pass-Safe for your password management needs!")