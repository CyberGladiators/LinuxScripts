import subprocess


def is_minlen_set(line):

    params = line.split()
    for param in params:
        if param.startswith("minlen="):
            length = param.split("=")[1]
            if length.isdigit() and int(length) >= 8:
                return True
    return False

def passwdMinimumForDebian():
    try:

        subprocess.run(["sudo", "cp", "/etc/pam.d/common-password", "/etc/pam.d/common-password.bak"], check=True)

        with open("/etc/pam.d/common-password", "r") as file:
            lines = file.readlines()


        modified = False

        with open("/etc/pam.d/common-password", "w") as file:
            for line in lines:
                if "pam_unix.so" in line and not is_minlen_set(line):

                    file.write(line.strip() + " minlen=8\n")
                    modified = True
                else:
                    file.write(line)

        if modified:
            print("Password length requirement has been set.")
        else:
            print("Password length requirement was already set.")

    except PermissionError:
        print("You must run this script with sudo permissions.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


passwdMinimumForDebian()
