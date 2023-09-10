import os
import glob

def search_and_display_files():
    # Change '~/Desktop' to the full path if necessary
    directory = os.path.expanduser('~/Desktop')
    pattern = 'Forensics_Questions_*'

    # Search for files that match the pattern
    files = glob.glob(os.path.join(directory, pattern))

    # Display file contents
    for file in files:
        if os.path.isfile(file):
            print(f"Displaying contents of {file}:")
            with open(file, 'r') as f:
                print(f.read())
            print("-----\n")
    else: 
        print(" no Forensics_Questions found, something is probably wrong edit the cat_questions.py file to fix ")

# Call the function
search_and_display_files()
