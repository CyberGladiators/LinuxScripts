import subprocess

def remove_packages():
    try:
        print("Removing nmap, wireshark, john, and hydra...")
        subprocess.run(["sudo", "apt", "remove", "-y", "nmap", "wireshark", "john", "hydra"], check=True)
        print("Package removal complete.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {str(e)}")
