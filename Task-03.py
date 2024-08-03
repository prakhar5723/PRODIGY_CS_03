import string


def strength_checker(password):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    strength = 0

    if len(password) < 8:
        return "Password must be at least 8 characters long"

    if any(char in lower for char in password):
        strength += 1
    if any(char in upper for char in password):
        strength += 1
    if any(char in digits for char in password):
        strength += 1
    if any(char in special for char in password):
        strength += 1

    if len(password) >= 12:
        strength += 1
    if len(password) >= 16:
        strength += 1

    if strength == 1:
        return 'Very Weak'
    elif strength == 2:
        return 'Weak'
    elif strength == 3:
        return 'Good'
    elif strength == 4:
        return 'Strong'
    elif strength == 5:
        return 'Excellent'


if __name__ == "__main__":
    while True:
        password = input("Enter your password: ")
        rating = strength_checker(password)
        print(f"Password strength: {rating}")
