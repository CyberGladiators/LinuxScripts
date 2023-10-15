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

    # List of known system users (Add more as you see fit)
    system_users = ['root', 'daemon', 'bin', 'sys', 'sync', 'games', 'man', 'lp', 'mail',
                    'news', 'uucp', 'proxy', 'www-data', 'backup', 'list', 'irc',
                    'gnats', 'nobody', 'systemd-network', 'systemd-resolve', 'syslog',
                    'messagebus', '_apt', 'tss', 'sshd', 'landscape', 'pollinate', 'colord', 'whoopsie']

    check_users(allowed_users, system_users)

if __name__ == "__main__":
    check_unauthorized_users()
