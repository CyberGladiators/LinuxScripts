import subprocess


subprocess.run(["sudo", "cp", "/etc/pam.d/common-password", "/etc/pam.d/common-password.bak"], check=True)

def passwdMinimum():
    try:
        with open("/etc/pam.d/common-password", "r") as f:
            lines = f.readlines()

        with open("/etc/pam.d/common-password", "w") as f:
            for line in lines:
                if "pam_unix.so" in line:
                    f.write(line.strip() + " minlen=8\n")
                else:
                    f.write(line)

        print("Password length requirement has been set.")
    except PermissionError:
        print("You must run this script with sudo permissions.")
