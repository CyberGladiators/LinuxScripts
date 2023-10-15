import subprocess

def is_package_installed(package):
    try:
        subprocess.run(["dpkg", "-l", package], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def remove_package(package):
    try:
        print(f"Removing {package}...")
        subprocess.run(["sudo", "apt", "purge", "-y", package], check=True)
        print(f"{package} removal complete.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {str(e)}")

def remove_packages():
    packages = [
    "nmap", "metasploit-framework", "burpsuite", "john", "hydra", "sqlmap", "wireshark", 
    "aircrack-ng", "nikto", "gobuster", "dirb", "hashcat", "wpscan", "enum4linux", "netcat", 
    "openvpn", "ophcrack", "binwalk", "radare2", "masscan", "snort", "maltego", "cewl", 
    "recon-ng", "theharvester", "dnsrecon", "beef-xss", "cisco-torch", "etherape", "yersinia", 
    "zaproxy", "kismet", "hping3", "armitage", "netsniff-ng", "cuckoo", "volatility", "mimikatz",
    "setoolkit", "msfpc", "uniscan", "veil", "wifite", "responder", "empire", "mitmproxy",
    "patator", "medusa", "fcrackzip", "foremost", "sleuthkit", "autopsy", "chntpw", "flasm", 
    "macchanger", "truecrack", "tcpflow", "tcpreplay", "tcpdump", "sslyze", "powersploit",
    "reaver", "pixiewps", "photon", "lynis", "joomscan", "ettercap", "sslstrip", "slowhttptest",
    "skipfish", "seclists", "pyrit", "proxychains", "proxychains-ng", "samba"
]

    for package in packages:
        if is_package_installed(package):
            answer = input(f"{package} is installed. Do you want to remove it? (y/n): ")
            if answer.lower() == "y":
                remove_package(package)
            else:
                print(f"Skipping {package}...")
        else:
            print(f"{package} is not installed. Skipping...")

def check_and_remove_packages():
    remove_packages()

if __name__ == "__main__":
    check_and_remove_packages()
