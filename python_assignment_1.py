import re

# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength.
passwd = input("Please enter your password: ")


def check_password_strength(passwd):
    # Checking the length
    if len(passwd) < 8:
        return False
    # Checking Uppercase
    if not any(char.isupper() for char in passwd):
        return False
    # Checking Lowercase
    if not any(char.islower() for char in passwd):
        return False
    # Checking Number
    if not any(char.isdigit() for char in passwd):
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


# Calling the function and printing the output
print(provide_feedback(passwd))
