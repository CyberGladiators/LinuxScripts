import os


def find_txt_files_in_home():
    home_base = "/home"
    txt_files = []

    # Check if the base directory exists
    if not os.path.exists(home_base):
        print(f"Directory {home_base} does not exist.")
        return

    # Iterate through each user directory in /home
    for user_dir in os.listdir(home_base):
        full_path = os.path.join(home_base, user_dir)

        # Ensure it's a directory
        if os.path.isdir(full_path):
            # Walk through each directory and subdirectory
            for root, _, files in os.walk(full_path):
                for file in files:
                    # Check for .txt files (including hidden ones starting with '.')
                    if file.endswith(".txt"):
                        file_path = os.path.join(root, file)
                        txt_files.append(file_path)

    # Display all found .txt files with full paths
    if txt_files:
        print("Found .txt files (including hidden files):")
        for file_path in txt_files:
            print(file_path)  # Each file path is printed here
    else:
        print("No .txt files found in home directories.")


# Usage in main.py
if __name__ == "__main__":
    find_txt_files_in_home()
