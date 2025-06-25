import re

def analyze_password(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters for stronger security.")

    # Uppercase, lowercase, digits, and special characters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("Use at least one special character.")

    # Final evaluation
    print("\nPassword Score:", score, "/ 6")
    if score == 6:
        print(" Strong password!")
    else:
        print(" Weaknesses detected:")
        for tip in suggestions:
            print("-", tip)

# Main program loop
if __name__ == "__main__":
    user_input = input("Enter a password to analyze: ")
    analyze_password(user_input)
