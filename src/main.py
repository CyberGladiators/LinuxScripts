import subprocess
import os

from find import search_files  
from ssh_config import modify_ssh_config  

def main_options():
    print("Choose the main option you want to execute:")
    print("1. Search for files")
    print("2. Modify SSH Config")
    print("3. [Description for the third option]")
    print("4. [Description for the third option]")
    print("5. [Description for the third option]")
    print("6. [Description for the third option]")

    choice = input("Enter your choice: ")

    if choice == '1':
        search_files()
    elif choice == '2':
        modify_ssh_config()
    elif choice == '3':
        print("Executing the third option")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main_options()

