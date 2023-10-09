# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength.
def check_password_strength(passwd):
    if len(passwd) > 8:
        for char in passwd:
            return "The length of the password is less than 8 characters. Please try again!"
