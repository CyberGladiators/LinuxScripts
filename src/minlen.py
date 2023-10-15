import subprocess

subprocess.run(["sudo", "cp", "/etc/pam.d/common-password", "/etc/pam.d/common-password.bak"], check=True)

subprocess.run(["sudo", "cp", "/etc/security/pwquality.conf", "/etc/security/pwquality.conf.bak"], check=True)

def passwdMinimum():
    try:
        
        with open("/etc/pam.d/common-password", "r") as f:
            lines = f.readlines()

        with open("/etc/pam.d/common-password", "w") as f:
            for line in lines:
                if "pam_unix.so" in line and "pam_pwquality.so" not in line:
                    f.write("password requisite pam_pwquality.so retry=3\n")
                f.write(line)

        with open("/etc/security/pwquality.conf", "a") as f:
            f.write("minlen = 8\n")

        print("Password length requirement has been set.")
    except PermissionError:
        print("You must run this script with sudo permissions.")

passwdMinimum()
