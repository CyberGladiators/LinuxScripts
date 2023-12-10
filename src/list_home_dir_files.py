def list_all_files_in_home_with_path():
    home_dir = os.path.expanduser('~')
    ignore_dir = os.path.join(home_dir, "LinuxScripts")
    
    all_files = [os.path.join(home_dir, f) for f in os.listdir(home_dir) if os.path.isfile(os.path.join(home_dir, f)) and not f.startswith(ignore_dir)]
    
    if all_files:
        non_hidden_files = [f for f in all_files if not os.path.basename(f).startswith('.')]
        hidden_files = [f for f in all_files if os.path.basename(f).startswith('.')]
        
        print("\nNon-hidden files in the home directory with their paths:")
        for file in non_hidden_files:
            print(file)

        print("--------")
        
        print("Hidden files in the home directory with their paths:")
        for file in hidden_files:
            print(file)
    else:
        print("\nNo files found in the home directory.")
