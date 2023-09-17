import subprocess

def modify_ssh_config():
    # Backup the original sshd_config file
    subprocess.run(["cp", "/etc/ssh/sshd_config", "/etc/ssh/sshd_config.bak"])

    # Read the existing sshd_config lines
    with open("/etc/ssh/sshd_config", "r") as f:
        lines = f.readlines()

    # Modify the lines as needed
    new_lines = []
    for line in lines:
        if line.strip() == "PermitRootLogin yes":
            new_lines.append("PermitRootLogin no\n")
        elif "PermitEmptyPasswords" in line.strip():
            new_lines.append("PermitEmptyPasswords no\n")
        elif "X11Forwarding" in line.strip():
            new_lines.append("X11Forwarding no\n")
        elif "UsePAM" in line.strip():
            new_lines.append("UsePAM yes\n")
        else:
            new_lines.append(line)

    # Write the new lines to sshd_config
    with open("/etc/ssh/sshd_config", "w") as f:
        f.writelines(new_lines)

    # Restart the ssh service to apply the changes
    subprocess.run(["service", "ssh", "restart"])

# Uncomment the next line to run the function
# modify_ssh_config()
