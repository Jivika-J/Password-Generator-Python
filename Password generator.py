import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    selected_chars = ""
    password_chars = []

    if use_upper:
        selected_chars += string.ascii_uppercase
        password_chars.append(random.choice(string.ascii_uppercase))

    if use_lower:
        selected_chars += string.ascii_lowercase
        password_chars.append(random.choice(string.ascii_lowercase))

    if use_digits:
        selected_chars += string.digits
        password_chars.append(random.choice(string.digits))

    if use_symbols:
        selected_chars += string.punctuation
        password_chars.append(random.choice(string.punctuation))

    if not selected_chars:
        return "Error: Select at least one character type."

    if length < len(password_chars):
        return "Error: Password length too short for selected options."

    while len(password_chars) < length:
        password_chars.append(random.choice(selected_chars))

    random.shuffle(password_chars)
    return ''.join(password_chars)


# -------- Main Program --------
try:
    length = int(input("Enter password length: "))

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(
        length,
        use_upper,
        use_lower,
        use_digits,
        use_symbols
    )

    print("\nGenerated Password:", password)

except ValueError:
    print("Invalid input. Please enter numeric values where required.")

