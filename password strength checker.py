def check_password(password):

    if len(password) < 8:
        return "Weak: password is too short"

    if password.isalpha():
        return "Weak: use numbers and symbols too"

    if password.isdigit():
        return "Weak: use letters and symbols too"

    return "Password looks stronger"


password = input("Enter a password to check: ")

result = check_password(password)

print(result)
