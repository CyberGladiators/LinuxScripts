import subprocess

def update_system():
    try:
        print("Updating package list...")
        subprocess.run(["sudo", "apt", "update", "-y"], check=True)
        print("Upgrading packages...")
        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
        print("Performing distribution upgrade...")
        subprocess.run(["sudo", "apt", "dist-upgrade", "-y"], check=True)
        print("Removing unnecessary packages...")
        subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
        print("System update complete.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {str(e)}")
