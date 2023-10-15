import subprocess

def lightdm_configure():
    # Use lightdm-set-defaults to configure LightDM
    try:
        subprocess.run(["sudo", "lightdm-set-defaults", "--allow-guest", "false"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return

    # Restart LightDM to apply the changes
    try:
        subprocess.run(["sudo", "systemctl", "restart", "lightdm"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    lightdm_configure()
