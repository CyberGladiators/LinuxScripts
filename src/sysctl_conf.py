def update_sysctl_config():
    sysctl_config = """
    fs.file-max = 65535
    fs.protected_fifos = 2
    fs.protected_regular = 2
    fs.suid_dumpable = 0
    kernel.core_uses_pid = 1
    kernel.dmesg_restrict = 1
    kernel.exec-shield = 1
    kernel.sysrq = 0
    kernel.randomize_va_space = 2
    kernel.pid_max = 65536
    net.core.rmem_max = 8388608
    net.core.wmem_max = 8388608
    net.core.netdev_max_backlog = 5000
    net.ipv4.tcp_rmem = 10240 87380 12582912
    net.ipv4.tcp_window_scaling = 1
    net.ipv4.tcp_wmem = 10240 87380 12582912
    net.ipv4.conf.all.accept_redirects = 0
    net.ipv4.conf.all.accept_source_route = 0
    net.ipv4.conf.all.log_martians = 1
    net.ipv4.conf.all.redirects = 0
    net.ipv4.conf.all.rp_filter = 1
    net.ipv4.conf.all.secure_redirects = 0
    net.ipv4.conf.all.send_redirects = 0
    net.ipv4.conf.default.accept_redirects = 0
    net.ipv4.conf.default.accept_source_route = 0
    net.ipv4.conf.default.log_martians = 1
    net.ipv4.conf.default.rp_filter = 1
    net.ipv4.conf.default.secure_redirects = 0
    net.ipv4.conf.default.send_redirects = 0
    net.ipv4.icmp_echo_ignore_all = 1
    net.ipv4.icmp_echo_ignore_broadcasts = 1
    net.ipv4.icmp_ignore_bogus_error_responses = 1
    net.ipv4.ip_forward = 0
    net.ipv4.ip_local_port_range = 2000 65000
    net.ipv4.tcp_max_syn_backlog = 2048
    net.ipv4.tcp_synack_retries = 2
    net.ipv4.tcp_syncookies = 1
    net.ipv4.tcp_syn_retries = 5
    net.ipv4.tcp_timestamps = 0

    net.ipv6.conf.all.disable_ipv6 = 1
    net.ipv6.conf.default.disable_ipv6 = 1
    net.ipv6.conf.lo.disable_ipv6 = 1

    net.ipv6.conf.default.router_solicitations = 0
    net.ipv6.conf.default.accept_ra_rtr_pref = 0
    net.ipv6.conf.default.accept_ra_pinfo = 0
    net.ipv6.conf.default.accept_ra_defrtr = 0
    net.ipv6.conf.default.autoconf = 0
    net.ipv6.conf.default.dad_transmits = 0
    net.ipv6.conf.default.max_addresses = 1
    """

    sysctl_file = '/etc/sysctl.conf'

    try:
        with open(sysctl_file, 'a') as file:
            file.write(sysctl_config)
        print(f"Configurations appended successfully to {sysctl_file}")
    except PermissionError:
        print("Permission denied: You need to run this script as root.")
    except Exception as e:
        print(f"An error occurred: {e}")
