import time
from datetime import datetime

now = datetime.now()

print("*It’s 3 AM. You’re the overnight IT guy. Your boss just sent you a link to install a new tool — something about querying company files faster.*")
time.sleep(2)
print("\nWelcome to DocQuery Pro, please enter your name below.")
time.sleep(1)
user_name = input("Please enter your name below and press Enter:")

print(f"\nThanks, {user_name}. Installing DocQuery Pro...")
time.sleep(2)

print("Current Date and Time: ", now) #Will change this later to add "time awareness" dialogue