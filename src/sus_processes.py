import subprocess

def check_suspicious_scripts():
    """Check for suspicious running scripts on the system, list the user in charge, and the file location."""
    try:
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True, check=True)
        lines = result.stdout.splitlines()

        print("\nSuspicious Running Scripts")
        print("==========================")
        for line in lines:
            if 'python' in line or 'sh' in line or 'bash' in line:
                # Check for scripts running from unusual locations (e.g., /tmp, /var/tmp)
                if '/tmp' in line or '/var/tmp' in line or '/dev/shm' in line:
                    parts = line.split()
                    user = parts[0]
                    script_location = parts[-1]
                    print(f"User: {user}, Script: {script_location}, Full Line: {line}")
    except subprocess.CalledProcessError:
        print("Failed to retrieve running processes. Please check your permissions.")
if __name__ == "__main__":
    check_suspicious_scripts()
