import random
import string

def generate_password(length=12):
    """Generate a secure password based on given rules."""
    if length < 8:
        length = 8  # Ensure minimum length of 8 characters
    
    # Define character pools
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensure at least one of each required character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password length with random choices from all character types
    all_chars = uppercase + lowercase + digits + special_chars
    while len(password) < length:
        new_char = random.choice(all_chars)
        
        # Avoid predictable sequences like "1111", "abcd", "1234"
        if len(password) >= 3 and password[-3:] == [new_char] * 3:
            continue  # Skip if the last three characters are identical
        
        password.append(new_char)
    
    # Shuffle to remove predictable patterns
    random.shuffle(password)
    
    password_str = "".join(password)
    return password_str

if __name__ == "__main__":
    password = generate_password()
    print("Generated Secure Password:", password)
