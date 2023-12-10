import subprocess

def is_package_installed(package):
    try:
        subprocess.run(["dpkg", "-l", package], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_package(package):
    try:
        print(f"Installing {package}...")
        subprocess.run(["sudo", "apt", "get", "-y", package], check=True)
        print(f"{package} installation complete.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {str(e)}")

def install_packages():
    packages = [
    "deborphan", "micro", "vim", "clamscan", "clamtk"
    ]
    
    for package in packages:
        if not is_package_installed(package):
            answer = input(f"{package} is not installed. Do you want to install it? (y/n): ")
            if answer.lower() == "y":
                install_package(package)
            else:
                print(f"Skipping {package}...")
        else:
            print(f"{package} is already installed. Skipping...")

def check_and_install_packages():
    install_packages()

if __name__ == "__main__":
    check_and_install_packages()
