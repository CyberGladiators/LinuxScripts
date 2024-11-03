import os
import subprocess

def configure_account_lockout_policy():
    # Paths to the configuration files
    failloсk_file = "/usr/share/pam-configs/faillock"
    failloсk_notify_file = "/usr/share/pam-configs/faillock_notify"

    # Configuration text for faillock
    failloсk_content = """Name: Enforce failed login attempt counter
Default: no
Priority: 0
Auth-Type: Primary
Auth:
\trequired\tpam_faillock.so authfail
\tsufficient\tpam_faillock.so authsucc
"""

    # Configuration text for faillock_notify
    failloсk_notify_content = """Name: Notify on failed login attempts
Default: no
Priority: 1024
Auth-Type: Primary
Auth:
\trequisite\tpam_faillock.so preauth
"""

    # Create and write to the faillock file
    try:
        with open(failloсk_file, 'w') as f:
            f.write(failloсk_content)
        print(f"Configured {failloсk_file} successfully.")
    except PermissionError:
        print("Permission denied. Run the script with sudo or as root.")
        return
    except Exception as e:
        print(f"Error configuring {failloсk_file}: {e}")
        return

    # Create and write to the faillock_notify file
    try:
        with open(failloсk_notify_file, 'w') as f:
            f.write(failloсk_notify_content)
        print(f"Configured {failloсk_notify_file} successfully.")
    except PermissionError:
        print("Permission denied. Run the script with sudo or as root.")
        return
    except Exception as e:
        print(f"Error configuring {failloсk_notify_file}: {e}")
        return

    # Run pam-auth-update to apply the configuration
    try:
        print("Running pam-auth-update. Please follow the prompts to enable the required options.")
        subprocess.run(["sudo", "pam-auth-update"], check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to run pam-auth-update. Please ensure you have the required permissions.")
    except Exception as e:
        print(f"An error occurred while running pam-auth-update: {e}")

# Usage in main.py
if __name__ == "__main__":
    configure_account_lockout_policy()
