import subprocess
import os
import pwd
import glob

from find import search_files  
from ssh_config import modify_ssh_config  
from minlen import passwdMinimum
from crontab_find import list_crontabs
from cat_questions import search_and_display_files
from lightdm_conf import lightdm_configure
from update import update_system
from remove import remove_packages
from unauthusers import check_unauthorized_users
from changepasswd import change_passwords
from sysctl_conf import update_sysctl_config
from disableFTPwriteCommands import disable_ftp_write_commands
from logindefs import update_login_defs

def display_ascii_art(file_path):
    with open(file_path, 'r') as file:
        ascii_art = file.read()
    print(ascii_art)

display_ascii_art('ascii_art.txt')

def main_options():
    try:
        print("Choose the main option you want to execute:")
        print("1. Search for files")
        print("2. Modify SSH Config")
        print("3. add minimum passwd of 8")
        print("4. remove packages")
        print("5. list all the Forensics Questions")
        print("6. find all users crontabs")
        print("7. Lightdm configure")
        print("8. update the system ")
        print("9. list unauth users")
        print("10. change all user passwords")
        print("11. update sysctl conf file")
        print("12. disable FTP write commands")
        print("13. set password age in login defs")

        choice = input("$ ")

        if choice == '1':
            search_files()
        elif choice == '2':
            modify_ssh_config()
        elif choice == '3':
            passwdMinimum()
        elif choice == '4':
             remove_packages()
        elif choice == '5':
            search_and_display_files()
        elif choice == '6':
            list_crontabs()
        elif choice == '7':
            lightdm_configure()  
        elif choice == '8':
            update_system()  
        elif choice == '9':
            check_unauthorized_users()  
        elif choice == '10':
            change_passwords()
        elif choice == '11':
            update_sysctl_config()
        elif choice == '12':
            disable_ftp_write_commands()
        elif choice == "13":
            update_login_defs()
        else:
            print("Invalid choice")


    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully.")
        exit(0)
if __name__ == "__main__":
    main_options()
