import subprocess

def lightdm_configure():
    subprocess.run(["sudo", "cp", "/etc/lightdm/lightdm.conf", "/etc/lightdm/lightdm.conf.bak"], check=True)


    with open("/etc/lightdm/lightdm.conf", "a") as f:
        f.write("\nallow-guest=false\n")


    subprocess.run(["sudo", "service", "lightdm", "restart"], check=True)
