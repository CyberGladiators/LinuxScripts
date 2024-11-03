def remove_nullok_option():
    config_file = "/etc/pam.d/common-auth"
    search_line = "auth [success=2 default=ignore] pam_unix.so"
    nullok_option = "nullok"

    # Read the contents of the file
    with open(config_file, 'r') as file:
        lines = file.readlines()

    # Modify the line if it contains the search_line
    modified = False
    for i, line in enumerate(lines):
        if search_line in line and nullok_option in line:
            # Remove the 'nullok' option
            lines[i] = line.replace(nullok_option, "").strip() + "\n"
            modified = True
            break

    # Write back the changes if modified
    if modified:
        with open(config_file, 'w') as file:
            file.writelines(lines)
        print("Null passwords disabled: 'nullok' option removed.")
    else:
        print("'nullok' option already removed or line not found.")


# Usage in main.py
if __name__ == "__main__":
    remove_nullok_option()
