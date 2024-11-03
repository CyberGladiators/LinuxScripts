import subprocess


def enforce_password_policy():
    config_file = "/etc/pam.d/common-password"
    search_keyword = "pam_pwquality.so"
    minlen_option = "minlen=10"

    # Read the contents of the file
    with open(config_file, 'r') as file:
        lines = file.readlines()

    # Modify the line if it contains the search_keyword
    modified = False
    for i, line in enumerate(lines):
        print(f"Checking line {i}: {line.strip()}")  # Debugging output
        if search_keyword in line:
            if minlen_option not in line:
                lines[i] = line.strip() + f" {minlen_option}\n"
                modified = True
                print(f"Modified line {i} to include {minlen_option}")  # Debugging output
            else:
                print("Minlen option already set in this line.")  # Debugging output
            break

    # Write back the changes if modified
    if modified:
        with open(config_file, 'w') as file:
            file.writelines(lines)
            file.flush()  # Ensure data is written
        print("Password policy enforced: Minimum length set to 10.")
    else:
        print("Password policy already enforced or line not found.")

if __name__ == "__main__":
    enforce_password_policy()
