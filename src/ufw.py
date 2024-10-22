import subprocess

def setup_ufw():
    """Check if UFW is installed, install if not, and enable it."""
    def is_ufw_installed():
        try:
            subprocess.run(["ufw", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def install_ufw():
        try:
            print("UFW is not installed. Installing UFW...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "ufw", "-y"], check=True)
            print("UFW has been installed successfully.")
        except subprocess.CalledProcessError:
            print("Failed to install UFW. Please check your package manager or permissions.")

    def is_ufw_enabled():
        try:
            result = subprocess.run(["sudo", "ufw", "status"], check=True, capture_output=True, text=True)
            return "Status: active" in result.stdout
        except subprocess.CalledProcessError:
            return False

    def enable_ufw():
        try:
            print("Enabling UFW...")
            subprocess.run(["sudo", "ufw", "enable"], check=True)
            print("UFW has been enabled successfully.")
        except subprocess.CalledProcessError:
            print("Failed to enable UFW. Please check your permissions.")

    if not is_ufw_installed():
        install_ufw()
    else:
        print("UFW is already installed.")

    if not is_ufw_enabled():
        enable_ufw()
    else:
        print("UFW is already enabled.")

if __name__ == "__main__":
    setup_ufw()
