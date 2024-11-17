import re


def enforce_password_policy():
    config_file = "/etc/pam.d/common-password"
    search_keyword = "pam_pwquality.so"
    minlen_option = "minlen=10"

    try:
        # Read the contents of the file
        with open(config_file, "r") as file:
            lines = file.readlines()

        # Track whether the file was modified
        modified = False

        # Process each line to ensure the minlen option is set
        for i, line in enumerate(lines):
            if search_keyword in line:
                # Check if minlen is already set
                if re.search(r"minlen=\d+", line):
                    # Update the minlen value to 10
                    lines[i] = re.sub(r"minlen=\d+", minlen_option, line)
                else:
                    # Append minlen=10 to the line
                    lines[i] = line.strip() + f" {minlen_option}\n"
                modified = True
                break

        # If no line with pam_pwquality.so is found, append a new configuration
        if not modified:
            lines.append(f"password requisite {search_keyword} {minlen_option}\n")
            modified = True

        # Write back the changes if modified
        if modified:
            with open(config_file, "w") as file:
                file.writelines(lines)
            print("Password policy enforced: Minimum length set to 10.")
        else:
            print("Password policy already enforced.")

    except PermissionError:
        print("Permission denied: You need to run this script as root.")
    except FileNotFoundError:
        print(f"Configuration file not found: {config_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    enforce_password_policy()
