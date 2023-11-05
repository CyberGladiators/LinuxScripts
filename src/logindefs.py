import re

def update_login_defs():
    with open("/etc/login.defs", "r") as file:
        content = file.read()
    
    # Update PASS_MAX_DAYS
    content = re.sub(r'PASS_MAX_DAYS.*', 'PASS_MAX_DAYS 90', content)
    
    # Update PASS_MIN_DAYS
    content = re.sub(r'PASS_MIN_DAYS.*', 'PASS_MIN_DAYS 10', content)

    # Update PASS_WARN_AGE
    content = re.sub(r'PASS_WARN_AGE.*', 'PASS_WARN_AGE 7', content)
    
    with open("/etc/login.defs", "w") as file:
        file.write(content)

if __name__ == "__main__":
    update_login_defs()
