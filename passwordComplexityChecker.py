# checks the password for complexity
"""
1. At least 8 characters—the more characters, the better.
2. A mixture of both uppercase and lowercase letters.
3. A mixture of letters and numbers.
4. Inclusion of at least one special character, e.g., ! @ # ? ].
5. password should not contain name, username, or company name.
"""

import re as r


def passwordComplexityChecker(password, username, company_name, name):
    strength = 175
    message = ""
    if len(password) < 8:
        strength -= 50
        message += "Password should be at least 8 characters long.\n"
    if not r.search(r"[a-z]", password):
        strength -= 25
        message += "Password should contain at least one lowercase letter.\n"
    if not r.search(r"[A-Z]", password):
        strength -= 25
        message += "Password should contain at least one uppercase letter.\n"
    if not r.search(r"[0-9]", password):
        strength -= 25
        message += "Password should contain at least one number.\n"
    if not r.search(r"[!@#?]", password):
        strength -= 25
        message += "Password should contain at least one special character.\n"
    if username in password or company_name in password or name in password:
        strength -= 25
        message += "Password should not contain name, username, or company name.\n"
    if len(password) > 10:
        strength += 25
    return strength, message


if __name__ == "__main__":
    password = input("Enter the password: ")
    username = input("Enter the username: ")
    company_name = input("Enter the company name: ")
    name = input("Enter the name: ")
    strength, message = passwordComplexityChecker(password, username, company_name, name)
    if strength < 50:
        print("Password is weak.")
        print(message)
    elif strength == 150:
        print("Password is moderate.")
        print(message)
    elif strength > 175:
        print("Password is strong as superman.")
        print(message)
    else:
        print("Password is strong.")
        print(message)
