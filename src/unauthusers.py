def read_allowed_users(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def check_users(allowed_users, system_users):
    unknown_users = []
    sys_users = []
    
    with open('/etc/passwd', 'r') as file:
        lines = file.readlines()

    print("Unknown Users")
    print("=============")
    for line in lines:
        if not line.startswith('#'):
            username = line.split(':')[0]
            if username not in allowed_users:
                if username in system_users:
                    sys_users.append(username)
                else:
                    print(f'Unauthorized user: {username}')
                    unknown_users.append(username)
                    
    print("\nSystem Users")
    print("============")
    for user in sys_users:
        print(f'System user: {user}')

def check_unauthorized_users():
    # List of allowed users
    allowed_users = read_allowed_users('users.txt')

  system_users = ['root', 'daemon', 'bin', 'sys', 'sync', 'games', 'man', 'lp', 'mail',
                    'news', 'uucp', 'proxy', 'www-data', 'backup', 'list', 'irc',
                    'gnats', 'nobody', 'systemd-network', 'systemd-resolve', 'syslog',
                    'messagebus', '_apt', 'tss', 'sshd', 'landscape', 'pollinate', 'colord', 'whoopsie']

system_users.extend(['usbmux', 'rtkit', 'lightdm', 'avahi-autoipd', 'avahi', 'kernoops', 'rtkit', 'speech-dispatcher', 'rtkit', 'avahi-autoipd', 'avahi', 'gdm', 'gnome-initial-setup', 'hplip', 'kernoops', 'rtkit', 'whoopsie', 'avahi-autoipd', 'avahi', 
                         'gnome-initial-setup', 'gdm', 'rtkit', 'kernoops', 'saned', 'pulse', 'pulse-access', 'rtkit', 'speech-dispatcher', 'whoopsie', 'kernoops', 'saned', 'geoclue', 'rtkit', 'colord', 'rtkit', 'geoclue', 'gnome-initial-setup', 'gdm', 'lightdm', 'rtkit', 'sddm', 'gdm', 'whoopsie', 'colord', 'saned', 'rtkit', 'speech-dispatcher',
                         'systemd-coredump', 'systemd-network', 'systemd-resolve', 'syslog', 'polkitd', 'avahi-autoipd', 'avahi', 
                         'geoclue', 'gnome-initial-setup', 'rtkit', 'gdm', 'lightdm', 'kernoops', 'saned', 'gnome', 'libvirt-qemu', 'libvirt-dnsmasq', 'tss', 'sshd', 'usbmux', 'avahi-autoipd', 'avahi', 'geoclue', 'gdm', 'gnome-initial-setup','gnome', 'hplip', 'kernoops', 
                         'lightdm', 'polkitd', 'rtkit', 'saned', 'speech-dispatcher', 'sddm', 'systemd-network', 'systemd-resolve', 'syslog', 
                         'usbmux', 'whoopsie', 'colord', 'geoclue', 'gnome-initial-setup', 'gnome', 'gdm', 'lightdm', 'polkitd', 'rtkit', 'sddm', 'saned', 'speech-dispatcher', 'usbmux', 'rtkit', 'lightdm', 'avahi-autoipd', 'avahi', 'gnome-initial-setup', 'gnome', 'rtkit', 'kernoops', 'saned', 'whoopsie'])

# Please note that the list of system users may vary depending on your specific system and installed software.

    check_users(allowed_users, system_users)

if __name__ == "__main__":
    check_unauthorized_users()
