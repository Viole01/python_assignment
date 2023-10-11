import re, psutil, sys  # re = regular expression library; sys = library used to access CLI arguments


# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength.
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


# Calling the function only when the script is run directly and printing the output
if __name__ == "__main__":
    passwd = input("Please enter your password: ")
    print(provide_feedback(passwd))

# Q2. As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU.


# print(type(psutil.cpu_percent())) Checked the data type
def monitor_cpu(threshold):
    try:  # Using try block for error handling..
        while True:  # Setting an infinite loop for application to run until interrupted
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU usage is {cpu_usage}%")
            if cpu_usage > threshold:
                print(f"Alert: CPU usage exceeding {threshold}")

    except KeyboardInterrupt:
        print(f"\nMonitoring stopped by user")

    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    threshold = 75  # Setting default threshold value as 75%
    monitor_cpu(threshold)

# Q4. Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.
src_path = sys.argv[1]
dest_path = sys.argv[2]


def take_backup(src, dest):
    print(src, dest)


take_backup(src_path, dest_path)
