import os

def check_and_delete_sudo_users():
    # Get list of users in the sudo group
    with open('/etc/group', 'r') as file:
        lines = file.readlines()

    sudo_users = []
    for line in lines:
        if line.startswith('sudo:'):  # Find the sudo group line
            sudo_users = line.strip().split(':')[-1].split(',')
            break

    if not sudo_users or sudo_users == ['']:
        print("No sudo users found.")
    else:
        print("The following users have sudo privileges:")
        for user in sudo_users:
            print(f"- {user}")
            choice = input(f"Do you want to delete {user} from the sudo group? (y/n): ")
            if choice.lower() == 'y':
                os.system(f'sudo gpasswd -d {user} sudo')
                print(f"{user} has been removed from the sudo group.")
            else:
                print(f"{user} has not been removed.")


if __name__ == "__main__":
    check_and_delete_sudo_users()
