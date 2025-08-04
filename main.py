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

choice = input("\nDo you want to install folder on your pc? (yes/no): ").strip().lower()

if choice == "yes":
    print(f"Sounds good {user_name}, now creating folder...")
elif choice == "no":
    print(f"You have selected no. I'm disappointed {user_name}. Installing anyway...")
else:
    print("\nI didn't catch that, so auto installing...")

print(f"Attempting to create folder at: {folder_path}")


if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("\nA new folder has appeared on your Desktop.")
else:
    print("\nThat folder is already on your Desktop.")

time.sleep(2) 