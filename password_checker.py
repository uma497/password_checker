import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count satisfied conditions
    checks = [not length_error, not digit_error, not uppercase_error, not lowercase_error, not symbol_error]
    strength = sum(checks)

    # Feedback
    if strength == 5:
        remarks = "💪 Strong password"
    elif 3 <= strength < 5:
        remarks = "⚠️ Moderate password. Improve it."
    else:
        remarks = "❌ Weak password! Please change it."

    # Show missing criteria
    issues = []
    if length_error:
        issues.append("At least 8 characters")
    if digit_error:
        issues.append("At least 1 digit")
    if uppercase_error:
        issues.append("At least 1 uppercase letter")
    if lowercase_error:
        issues.append("At least 1 lowercase letter")
    if symbol_error:
        issues.append("At least 1 special symbol (!@#$...)")

    return strength, remarks, issues


def main():
    password = input("Enter your password to evaluate: ")
    strength, remarks, issues = check_password_strength(password)

    print(f"\nPassword Strength: {strength}/5")
    print(remarks)
    if issues:
        print("🔑 Improve your password by adding:")
        for issue in issues:
            print(f"  - {issue}")


if __name__ == "__main__":
    main()
