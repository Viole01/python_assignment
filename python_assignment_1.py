import re  # Using regular expression for pattern matching in strings

# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength.
passwd = input("Please enter your password: ")


def check_password_strength(passwd):
    # Minimum length check
    if len(passwd) < 8:
        return False
    # Uppercase Check
    for char in passwd:
        if not char.isupper():
            return False
    # Lowercase Check
    for char in passwd:
        if not char.islower():
            return False
    # Digit Check
    for char in passwd:
        if not char.isdigit():
            return False
    # Special Character Check
    special_chars = r"[!@#$%^&*(),.?\":{}|<>]"
    if not re.search(special_chars, passwd):
        return False

    return True


def provide_feedback(passwd):
    if check_password_strength(passwd):
        return "Your Password is strong!"
    else:
        return "Please check your password, make sure it meets all the criteria."


# Callinf the function and printing the output
print(provide_feedback(passwd))
