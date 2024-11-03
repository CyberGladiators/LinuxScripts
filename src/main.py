import subprocess
import os
import pwd
import glob

from find import search_files  
from ssh_config import modify_ssh_config  
from minlen import enforce_password_policy
from crontab_find import list_cron_jobs
from cat_questions import search_and_display_files
from lightdm_conf import lightdm_configure
from update import update_system
from remove import remove_packages
from unauthusers import check_unauthorized_users
from changepasswd import change_passwords
from sysctl_conf import update_sysctl_config
from disableFTPwriteCommands import disable_ftp_write_commands
from logindefs import update_login_defs
from list_home_dir_files import find_txt_files_in_home
from ufw import setup_ufw
from sus_processes import check_suspicious_scripts
from remove_sudo_users import check_and_delete_sudo_users
from chrome_popup import block_chrome_popups
from common_auth_nullok import remove_nullok_option
from change_major_file_permissions import check_and_fix_permissions
from list_sus_connections import list_suspicious_connections
from configure_account_lockout_policy import configure_account_lockout_policy

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
        print("14. list all hidden files in home directory")
        print("15. enable and install ufw")
        print("16. check for suspicious scripts")
        print("17. remove sudo users")
        print("18. enable chrome popups")
        print("19. pam.d common auth remove nullok")
        print("20. change major file permissions")
        print("21. list sus connections")
        print("22. configure account lockout policy")
        choice = input("$ ")

        if choice == '1':
            search_files()
        elif choice == '2':
            modify_ssh_config()
        elif choice == '3':
            enforce_password_policy()
        elif choice == '4':
             remove_packages()
        elif choice == '5':
            search_and_display_files()
        elif choice == '6':
            list_cron_jobs()
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
        elif choice == "14":
            find_txt_files_in_home()
        elif choice == "15":
            setup_ufw()
        elif choice == "16":
            check_suspicious_scripts()
        elif choice == "17":
            check_and_delete_sudo_users()
        elif choice == "18":
            block_chrome_popups()
        elif choice == "19":
            remove_nullok_option()
        elif choice == "20":
            check_and_fix_permissions()
        elif choice == "21":
            list_suspicious_connections()
        elif choice == "22":
            configure_account_lockout_policy()
        else:
            print("Invalid choice")


    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully.")
        exit(0)
if __name__ == "__main__":
    main_options()
