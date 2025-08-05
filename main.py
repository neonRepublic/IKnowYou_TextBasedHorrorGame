import time
from datetime import datetime
import os

desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
install_folder = "IKnowYou"
folder_path = os.path.join(desktop_path, install_folder)

print("*It’s 3 AM. You’re the overnight IT guy. Your boss just sent you a link to install a new tool — something about querying company files faster.*")
time.sleep(2)
print("\nWelcome to DocQuery Pro, please enter your name below.")
time.sleep(1)
user_name = input("Please enter your name below and press Enter:")

print(f"\nThanks, {user_name}. Installing DocQuery Pro...")
time.sleep(2)

now = datetime.now()
print("Current Date and Time: ", now)
time.sleep(1)
print(f"\nWow, would you look at the time {user_name}")
time.sleep(1)

choice = input("\nWould you like to install a shortcut? (yes/no): ").strip().lower()

if choice == "yes":
    print(f"Sounds good {user_name}, now creating folder...")
elif choice == "no":
    print(f"You have selected no. I'm disappointed {user_name}. Installing anyway...")
else:
    print("\nI didn't catch that, so auto installing...")

print(f"Attempting to create folder at: {folder_path}")


if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("Attempting to create a new folder on your Desktop...")
else:
    print("\nThat folder is already on your Desktop...")

time.sleep(2) 

print("Do not try to delete this file or there will be repercussions")

second_choice = input(f"Do you understand, {user_name}? (yes/no): ").strip().lower()

if second_choice == "yes":
    print(f"I knew you would understand, I think we'll get along just fine {user_name}")
elif second_choice == "no":
    print(f"I dare you to try...")
else:
    print(f"That was not an option but I'll assume you understand {user_name}")
