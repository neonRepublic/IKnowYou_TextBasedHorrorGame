import time
from datetime import datetime
import os

now = datetime.now()
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
install_folder = "InstallFolder"
folder_path = os.path.join(desktop_path, install_folder)

print("*It’s 3 AM. You’re the overnight IT guy. Your boss just sent you a link to install a new tool — something about querying company files faster.*")
time.sleep(2)
print("\nWelcome to DocQuery Pro, please enter your name below.")
time.sleep(1)
user_name = input("Please enter your name below and press Enter:")

print(f"\nThanks, {user_name}. Installing DocQuery Pro...")
time.sleep(2)

print("Current Date and Time: ", now) #Will change this later to add "time awareness" dialogue
time.sleep(1)
print(f"\nWow, would you look at the time {user_name}")
time.sleep(1)

choice = input("\nDo you want to install folder on your pc? (yes/no): ").strip().lower()

if choice == "yes":
    print(f"Sounds good {user_name}, Now creating folder...")
elif choice == "no":
    print(f"You have selected no. I'm dissapointed {user_name}. Installing anyway...")
else:
    print("\nI didn't catch that, so auto installing...")