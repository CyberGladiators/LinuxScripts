import subprocess

def modify_ssh_config():

    subprocess.run(["cp", "/etc/ssh/sshd_config", "/etc/ssh/sshd_config.bak"])

    # Read the existing sshd_config lines
    with open("/etc/ssh/sshd_config", "r") as f:
        lines = f.readlines()

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
        elif line.strip().startswith("Protocol"):
            new_lines.append("Protocol 2\n")
        elif line.strip().startswith("HostbasedAuthentication"):
            new_lines.append("HostbasedAuthentication no\n")
        elif line.strip().startswith("IgnoreRhosts"):
            new_lines.append("IgnoreRhosts yes\n")
        elif line.strip().startswith("Ciphers"):
            new_lines.append("Ciphers aes256-ctr,aes192-ctr,aes128-ctr\n")
        elif line.strip().startswith("LoginGraceTime"):
            new_lines.append("LoginGraceTime 60\n")
        elif line.strip().startswith("Compression"):
            new_lines.append("Compression no\n")
        elif line.strip().startswith("MaxAuthTries"):
            new_lines.append("MaxAuthTries 3\n")
        elif line.strip().startswith("LogLevel"):
            new_lines.append("LogLevel INFO\n")
        else:
            new_lines.append(line)

    with open("/etc/ssh/sshd_config", "w") as f:
        f.writelines(new_lines)

    subprocess.run(["service", "ssh", "restart"])

try:
    with open("/etc/ssh/sshd_config", "r") as f:
        lines = f.readlines()
    # Rest of your code...
except FileNotFoundError as e:
    print(f"Error opening file: {e}")
    print("Please check the file path and permissions.")

# Uncomment the next line to run the function
# modify_ssh_config()
