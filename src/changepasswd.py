import subprocess

def change_passwords():
    try:
        with open('users.txt', 'r') as file:
            usernames = file.readlines()

        for username in usernames:
            username = username.strip()
            if username:
                print(f"Changing password for {username}...")
                cmd = f"echo '{username}:CyberGlads@1' | sudo chpasswd"
                subprocess.run(cmd, shell=True, check=True)
        
        print("Password changes complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

