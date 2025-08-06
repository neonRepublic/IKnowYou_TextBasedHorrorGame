import time
from datetime import datetime
import os
import getpass
import socket
import uuid
import json

desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
install_folder = "IKnowYou"
folder_path = os.path.join(desktop_path, install_folder)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("\n*It’s your first day as the new IT guy. Your boss just sent you a link to install a tool — something about querying company files faster.*\n")
time.sleep(2)

logo = r"""
  _____              ____                         
 |  __ \            / __ \                        
 | |  | | ___   ___| |  | |_   _  ___ _ __ _   _  
 | |  | |/ _ \ / __| |  | | | | |/ _ \ '__| | | | 
 | |__| | (_) | (__| |__| | |_| |  __/ |  | |_| | 
 |_____/_\___/ \___|\___\_\\__,_|\___|_|   \__, | 
   |  __ \                                  __/ | 
   | |__) | __ ___                         |___/  
   |  ___/ '__/ _ \                               
   | |   | | | (_) |                              
   |_|   |_|  \___/      
                                  
            ™️  // DocQuery Pro v3.7
"""
print(logo)
time.sleep(2)

print("\nWelcome to DocQuery Pro, please enter your name below.\n")
time.sleep(1)
user_name = input("Please enter your name below and press Enter:")

print(f"\nThanks, {user_name}. Installing DocQuery Pro...")
time.sleep(2)

now = datetime.now()
current_hour = now.hour

print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
time.sleep(1)

if 5 <= current_hour < 12:
    print(f"\nEarly start, {user_name}. Let's hope today goes... according to plan.")
elif 12 <= current_hour < 17:
    print(f"\nGood Morning, {user_name}. Let's begin.")
elif 17 <= current_hour < 22:
    print(f"\nWow, would you look at the time {user_name}\n")
else:
    print(f"\n{user_name}, it's the dead of night. The veil is thinner now.")    
time.sleep(2)

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
    print(f"\nThat was not an option but I'll assume you understand, {user_name}\n")
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
time.sleep(2)
print(f"\n*It reads: URGENT: {user_name} don't install the software! There's something wrong with it!*\n")
time.sleep(2)

print(f"\nIgnore that email, {user_name}...I mean it.\n")
time.sleep(2)

mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff)
                        for i in range(0, 8*6, 8)][::-1])

I_Know_You = (
    f"User: {user_name}\n"
    f"Username Entered: {username}\n"
    f"Password Entered: {password}\n"
    f"IP Address: {ip_address}\n"
    f"MAC Address: {mac_address}\n"
    f"Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')}\n"
    "\nI Know You\n"
)

data = {
    "User": user_name,
    "Username": username,
    "Password": password,
    "IP Address": ip_address,
    "MAC Address": mac_address,
    "Timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
    "Note": "I Know You"
}

print("\n*The screen flickers...*\n")
time.sleep(2)
print("*Something's happening in the background...*\n")
time.sleep(2)
print("*You feel a chill crawl down your spine.*\n")
time.sleep(3)

file_path = os.path.join(folder_path, "I_Know_You.txt")
with open(file_path, "w") as f:
    f.write(I_Know_You)

json_path = os.path.join(folder_path, "I_Know_You.json")
with open(json_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"File created.\n")
time.sleep(2)

print("You really thought no one was watching when you typed that password?")
time.sleep(3)
print("The hesitation... the backspace... the little sigh.")
time.sleep(4)
print("I saw all of it.")
time.sleep(3)
print("I see you.")
time.sleep(3)
print("And now...")
time.sleep(2)
print("I know *exactly* where you are.\n")
print('\a')
print('\a')
print('\a')
print('\a')
time.sleep(2)
print("Don’t bother unplugging the router.\n")
time.sleep(2)

i_know_you_logo = r"""

d888888b      db   dD d8b   db  .d88b.  db   d8b   db 
  `88'        88 ,8P' 888o  88 .8P  Y8. 88   I8I   88 
   88         88,8P   88V8o 88 88    88 88   I8I   88 
   88         88`8b   88 V8o88 88    88 Y8   I8I   88 
  .88.        88 `88. 88  V888 `8b  d8' `8b d8'8b d8' 
Y888888P      YP   YD VP   V8P  `Y88P'   `8b8' `8d8'  
                                                      
                                                      
          db    db  .d88b.  db    db                  
          `8b  d8' .8P  Y8. 88    88                  
           `8bd8'  88    88 88    88                  
             88    88    88 88    88                  
             88    `8b  d8' 88b  d88                  
             YP     `Y88P'  ~Y8888P'                  

"""

print(i_know_you_logo)
time.sleep(3)