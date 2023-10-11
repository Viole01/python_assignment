import re, psutil, sys, os, shutil  # re = regular expression module; sys = module used to access CLI arguments; os & shutil = Used to perform basic and high-level file operations respectively
from datetime import datetime  # Importing Class datetime from module datetime


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
    # If all conditions are satisfied..
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
            cpu_usage = psutil.cpu_percent(
                interval=1
            )  # Gives output after an interval of 1 Sec
            print(f"Current CPU usage is {cpu_usage}%")
            if cpu_usage > threshold:
                print(f"Alert: CPU usage exceeding {threshold}")

    except KeyboardInterrupt:  # Outside Interruption
        print(f"\nMonitoring stopped by user")

    except Exception as e:  # All remaining eroors
        print(f"An error occured: {e}")


if __name__ == "__main__":
    threshold = 75  # Setting default threshold value as 75%
    monitor_cpu(threshold)

# Q4. Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.
src_path = sys.argv[1]
dest_path = sys.argv[2]


def take_backup(src, dest):
    try:
        if not os.path.exists(src):  # Checking if Source exists or not..
            print(f"Source directory {src} does not exist.")
            return
        if not os.path.exists(dest):  # Checking if Destination exists or not..
            print(f"Destination directory {dest} does not exist.")
            return

        # Creating paths for all files in "src" directory & also for "dest"
        for file_name in os.listdir(src):
            src_file = os.path.join(src, file_name)
            dest_file = os.path.join(dest, file_name)

            # Handling Duplicate files in destination
            while os.path.exists(dest_file):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                file_name, file_extension = os.path.splitext(
                    file_name
                )  # Split file name & extension
                dest_file = os.path.join(
                    dest, f"{file_name}_{timestamp}{file_extension}"
                )  # Renaming the file with appending the timestamp

            shutil.copy2(src_file, dest_file)  # Copying files
            print(f"File copied successfully from '{src}' to '{dest}'")

    except shutil.SameFileError as File_already_exists:  #
        print(f"File already exists in Destination: {File_already_exists}")
    except Exception as e:
        print(f"An error occurred: {e}")


take_backup(src_path, dest_path)
