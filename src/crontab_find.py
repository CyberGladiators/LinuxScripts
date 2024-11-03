import os

def list_cron_jobs():
    # Paths for various cron sources
    user_crontab_path = "/var/spool/cron/crontabs"
    system_crontab_file = "/etc/crontab"
    cron_d_dir = "/etc/cron.d"
    cron_periodic_dirs = {
        "cron.daily": "/etc/cron.daily",
        "cron.hourly": "/etc/cron.hourly",
        "cron.weekly": "/etc/cron.weekly",
        "cron.monthly": "/etc/cron.monthly",
    }

    # List to collect all cron jobs found
    all_cron_jobs = []

    # Check user-specific cron jobs
    if os.path.isdir(user_crontab_path):
        for user_file in os.listdir(user_crontab_path):
            user_file_path = os.path.join(user_crontab_path, user_file)
            with open(user_file_path, 'r') as f:
                jobs = f.readlines()
                all_cron_jobs.append((f"User-specific ({user_file})", jobs, user_file))

    # Check system-wide cron jobs in /etc/crontab
    if os.path.isfile(system_crontab_file):
        with open(system_crontab_file, 'r') as f:
            jobs = f.readlines()
            # Extract the user running the job in system crontab (6th column in /etc/crontab format)
            system_jobs = []
            for job in jobs:
                parts = job.split()
                if len(parts) >= 7 and parts[0][0] != '#':
                    user = parts[5]  # The user field in system crontab
                    system_jobs.append((job.strip(), user))
                else:
                    system_jobs.append((job.strip(), "root (default)"))
            all_cron_jobs.append(("System-wide (/etc/crontab)", system_jobs, "root"))

    # Check cron jobs in /etc/cron.d directory
    if os.path.isdir(cron_d_dir):
        for cron_file in os.listdir(cron_d_dir):
            cron_file_path = os.path.join(cron_d_dir, cron_file)
            with open(cron_file_path, 'r') as f:
                jobs = f.readlines()
                cron_d_jobs = []
                for job in jobs:
                    parts = job.split()
                    # In /etc/cron.d, the 6th column is typically the user
                    if len(parts) >= 7 and parts[0][0] != '#':
                        user = parts[5]
                        cron_d_jobs.append((job.strip(), user))
                    else:
                        cron_d_jobs.append((job.strip(), "root (default)"))
                all_cron_jobs.append((f"/etc/cron.d/{cron_file}", cron_d_jobs, "root"))

    # Check periodic cron jobs (daily, hourly, weekly, monthly)
    for period, path in cron_periodic_dirs.items():
        if os.path.isdir(path):
            jobs = os.listdir(path)
            # Periodic cron jobs generally run as root
            all_cron_jobs.append((f"Periodic ({period})", jobs, "root"))

    # Display all cron jobs found
    print("Cron Jobs in the System:")
    for source, jobs, user in all_cron_jobs:
        print(f"\n--- {source} (Run by: {user}) ---")
        if isinstance(jobs, list):
            for job in jobs:
                if isinstance(job, tuple):
                    print(f"Job: {job[0]}, User: {job[1]}")
                else:
                    print(job)
        else:
            print(jobs.strip())

# Usage in main.py
if __name__ == "__main__":
    list_cron_jobs()
