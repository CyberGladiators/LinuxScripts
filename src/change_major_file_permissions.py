import os

def check_and_fix_permissions():
    files_permissions = {
        "/etc/passwd": 0o644,
        "/etc/shadow": 0o640,
        "/etc/group": 0o644,
        "/etc/gshadow": 0o640,
        "/etc/ssh/ssh_config": 0o644,
        "/etc/ssh/sshd_config": 0o644,
        "/etc/pam.d/common-auth": 0o644,
        "/etc/pam.d/common-password": 0o644,
        "/etc/sudoers": 0o440,
        "/root": 0o700,
        "/boot/grub/grub.cfg": 0o600
    }

    for file, required_perm in files_permissions.items():
        try:
            current_perm = os.stat(file).st_mode & 0o777
            if current_perm != required_perm:
                print(f"File: {file} has permissions {oct(current_perm)}, which is insecure.")
                response = input(f"Would you like to fix permissions to {oct(required_perm)}? (y/n): ").strip().lower()
                if response == 'y':
                    os.chmod(file, required_perm)
                    print(f"Permissions changed to {oct(required_perm)} for {file}")
                else:
                    print(f"Skipped changing permissions for {file}.")
            else:
                print(f"File: {file} permissions are already secure ({oct(current_perm)})")
        except FileNotFoundError:
            print(f"File: {file} not found.")
        except PermissionError:
            print(f"Permission denied for {file}. Please run the script with sudo or as root.")
        except Exception as e:
            print(f"An error occurred with file {file}: {e}")

# Usage in main.py
if __name__ == "__main__":
    check_and_fix_permissions()
