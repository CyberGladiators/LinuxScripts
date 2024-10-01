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
    "reaver", "pixiewps", "photon", "joomscan", "ettercap", "sslstrip", "slowhttptest",
    "skipfish", "seclists", "pyrit", "proxychains", "proxychains-ng", "samba",
    "nipe", "dnschef", "commix", "feroxbuster", "bettercap", "subfinder", "amass",
    "sherlock", "shodan", "censys", "pwnedOrNot", "zoom", "xsser",
    "sublist3r", "whatweb", "wafw00f", "sqlninja", "sparta", "spectre-meltdown-checker",
    "social-engineer-toolkit", "shellnoob", "mitmf", "maltego", "magescan",
    "king-phisher", "iodine", "inguma", "hurl", "hexorbase",
    "hamster-sidejack", "golismero", "galleta", "fierce", "faraday", "eyewitness",
    "enumiax", "easy-creds", "dbd", "davtest", "darkstat", "dalfox", "cutter", "cuckoo",
    "cowpatty", "bully", "bluepot", "blindelephant", "blacksheep", "bbqsql", "backdoor-factory",
    "automater", "atscan", "arachni", "angryip", "androguard", "afl", "ace", "acccheck",
    "thc-pptp-bruter", "wfuzz", "oclgausscrack", "tshark", "exploitdb", "thc-ipv6",
    "nbtscan", "onesixtyone", "maskprocessor", "multiforcer", "rainbowcrack", "rcracki-mt",
    "thc-hydra", "johnny", "avet", "beelogger", "metasploit-payload-generator", "powersploit",
    "sbd", "zizzania", "eapmd5pass", "fern-wifi-cracker", "ghost-phisher", "mdk3", "pyrit",
    "wepbuster", "wifiphisher", "wifitap", "wifite", "wapiti", "webacoo", "websploit",
    "httptunnel", "intersect", "polenum", "powersploit", "ridenum", "smbmap", "spoolsample",
    "sslcaudit", "unix-privesc-check", "windows-exploit-suggester",
    "netsparker", "metagoofil", "lbd", "iptraf-ng", "hping3", "hexinject",
    "hexedit", "hashid", "hash-identifier", "hashcat-utils", "hashcat", "halberd", "gqrx",
    "gpp-decrypt", "goofile", "golismero", "gobuster", "goad", "gitrob", "gitmails",
    "fimap", "fiked", "fcrackzip", "faradaysec", "eyewitness", "enum4linux", "dnsenum",
    "dnmap", "dhcpig", "detectem", "davtest", "darkd0rk3r", "dagon", "cymothoa",
    "cutycapt", "cupp", "cuckoo", "crunch", "creddump7", "cowpatty", "commix", "chown",
    "chaosreader", "cdpsnarf", "cangibrina", "c5scan", "byepass", "btscanner", "brutex",
    "brutespray", "brutesh", "brut3k1t", "bro", "arjun", "admidio",
    "vfeed", "veil-framework", "veil", "netbus-pro", "ipscan", "driver-support", "beware-ircd",
    "teamviewer", "utorrent", "ftpscan", "freeciv"
    #aditional
    "samba", "postgresql", "apache", "apache2", "mysql", "php", "snmp", "pop3", "sendmail", "dovecot", "bind9", "nginx"
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
