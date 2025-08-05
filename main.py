import time
from datetime import datetime
import os
import getpass

desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
install_folder = "IKnowYou"
folder_path = os.path.join(desktop_path, install_folder)

print("\n*It’s 3 AM. You’re the overnight IT guy. Your boss just sent you a link to install a new tool — something about querying company files faster.*\n")
time.sleep(2)
print("\nWelcome to DocQuery Pro, please enter your name below.\n")
time.sleep(1)
user_name = input("Please enter your name below and press Enter:")

print(f"\nThanks, {user_name}. Installing DocQuery Pro...")
time.sleep(2)

now = datetime.now()
print("Current Date and Time: ", now)
time.sleep(1)
print(f"\nWow, would you look at the time {user_name}\n")
time.sleep(1)

choice = input("\nWould you like to install a shortcut? (yes/no): \n").strip().lower()

if choice == "yes":
    print(f"\nSounds good {user_name}, now creating folder...\n")
elif choice == "no":
    print(f"\nYou have selected no. I'm disappointed {user_name}. Installing anyway...\n")
else:
    print("\nI didn't catch that, so auto installing...\n")
time.sleep(2)
print(f"Attempting to create folder...")
time.sleep(2)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("\nFolder created.\n")
else:
    print("\nThat folder is already on your Desktop...\n")

time.sleep(2) 

print("Under no circumstances should you delete this folder.")
time.sleep(2)

second_choice = input(f"Do you understand, {user_name}? (yes/no): ").strip().lower()
time.sleep(1)
if second_choice == "yes":
    print(f"\nI just knew you would understand, I think we'll get along just fine, {user_name}\n")
elif second_choice == "no":
    print(f"\nI dare you to try...\n")
else:
    print("\nThat was not an option but I'll assume you understand, {user_name}\n")
time.sleep(2)

print(f"\nNow, let's create a Username and Password: \n")
time.sleep(1)
username = input("Username: ")
password = getpass.getpass("Password: ")

print("\nValidating credentials...\n")
time.sleep(2)
print(f"\nThat's a funny password {user_name}, I'll remember that...\n")
time.sleep(2)
print(f"\nPassword \"{password}\" committed to memory...\n")
time.sleep(3)
print("...you really thought I couldn't see that?")
time.sleep(3)

print("\n             *NEW EMAIL*         \n")
time.sleep(2)
print("\n*The email alert rattles your nerves....*\n")
time.sleep(2)
print("\n*It's from your boss...*\n")
time.sleep(1)
print(f"\n*It reads: URGENT: {user_name} don't install the software.*\n")
time.sleep(2)

print(f"\nIgnore that email, {user_name}...I mean it.\n")