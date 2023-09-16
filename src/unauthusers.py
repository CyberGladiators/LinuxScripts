def read_allowed_users(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def check_users(allowed_users):
    with open('/etc/passwd', 'r') as file:
        lines = file.readlines()

    for line in lines:
        if not line.startswith('#'):  # Skip comments
            username = line.split(':')[0]
            if username not in allowed_users:
                print(f'Unauthorized user: {username}')

# New wrapper function
def check_unauthorized_users():
    allowed_users = read_allowed_users('users.txt')
    check_users(allowed_users)

if __name__ == "__main__":
    check_unauthorized_users()
