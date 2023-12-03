import os
import subprocess

def enable_automatic_updates():
    # Check if script is run as root
    if os.getuid() != 0:
        print("This function must be run as root.")
        return

    # Install unattended-upgrades
    print("Installing unattended-upgrades...")
    run_command("apt-get install unattended-upgrades")

    # Reconfigure unattended-upgrades
    print("Reconfiguring unattended-upgrades...")
    run_command("dpkg-reconfigure unattended-upgrades -f noninteractive")

    # Edit /etc/apt/apt.conf.d/20auto-upgrades
    config_20 = """
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutocleanInterval "7";
APT::Periodic::Unattended-Upgrade "1";
"""
    with open("/etc/apt/apt.conf.d/20auto-upgrades", "w") as file:
        file.write(config_20)

    # Edit /etc/apt/apt.conf.d/50auto-upgrades
    config_50 = """
Unattended-Upgrade::Allowed-Origins {
    "${distro_id} stable";
    "${distro_id} ${distro_codename}-security";
    "${distro_id} ${distro_codename}-updates";
};

Unattended-Upgrade::Package-Blacklist {
    "libproxy1v5";  # since the school filter blocks the word proxy
};
"""
    with open("/etc/apt/apt.conf.d/50auto-upgrades", "w") as file:
        file.write(config_50)

    print("Automatic updates have been enabled!")