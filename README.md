Secure Password Generator

A Python script that generates strong, random passwords following secure password rules.

How It Works
Generates a password with a minimum length of 8 characters (default: 12).
Guarantees the password always includes:
At least one uppercase letter
At least one lowercase letter
At least one digit
At least one special character
Avoids predictable repeated sequences (e.g. "1111", "aaaa").
Shuffles the final password so character types aren't in a predictable order.
Concepts Used
The random and string modules
List manipulation and shuffling
Basic pattern-avoidance logic (checking for repeated characters)
Functions with default parameters
Notes

This project was built as part of the "Digital Egypt Clubs Initiative" (DECI) training program to practice core Python and cybersecurity fundamentals.
