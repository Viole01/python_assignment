# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength.
passwd = input("Please enter your password: ")


def check_password_strength(passwd):
    res = False
    if len(passwd) < 8:
        res = True
        return res
    for char in passwd:
        if char.isupper():
            res = True
            return res
    for char in passwd:
        if char.islower():
            res = True
            return res


check_password_strength(passwd)
