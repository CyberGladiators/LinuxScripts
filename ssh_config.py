
import subprocess

def modify_ssh_config():
    # Backup the original sshd_config file
    subprocess.run(["cp", "/etc/ssh/sshd_config", "/etc/ssh/sshd_config.bak"])

    # Change the PermitRootLogin line in the sshd_config file
    with open("/etc/ssh/sshd_config", "r") as f:
        lines = f.readlines()

    with open("/etc/ssh/sshd_config", "w") as f:
        for line in lines:
            if line.strip() == "PermitRootLogin yes":
                f.write("PermitRootLogin no\n")
            else:
                f.write(line)

    # Restart the ssh service to apply the changes
    subprocess.run(["service", "ssh", "restart"])
