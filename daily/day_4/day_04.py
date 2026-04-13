# Day 4 - TCP Port Scanner
# Goal: Understand TCP connections by scanning ports
# This is what nmap does at its core

import socket
import threading
from datetime import datetime

# Well-known ports and their services
KNOWN_PORTS = {
    21:   "FTP        (File Transfer)",
    22:   "SSH        (Secure Shell - remote access)",
    23:   "Telnet     (Insecure remote access)",
    25:   "SMTP       (Email sending)",
    53:   "DNS        (Domain Name System)",
    80:   "HTTP       (Web - unencrypted)",
    110:  "POP3       (Email receiving)",
    143:  "IMAP       (Email access)",
    443:  "HTTPS      (Web - encrypted)",
    445:  "SMB        (Windows file sharing)",
    3306: "MySQL      (Database)",
    3389: "RDP        (Remote Desktop - Windows)",
    5900: "VNC        (Remote Desktop)",
    8080: "HTTP-Alt   (Web alternate port)",
    8443: "HTTPS-Alt  (Secure web alternate)",
}

open_ports   = []
lock         = threading.Lock()

def scan_port(host, port, timeout=0.5):
    """
    Attempt TCP connection to host:port
    If connection succeeds → port is OPEN
    If connection refused  → port is CLOSED
    If timeout             → port is FILTERED (firewall)
    """
    try:
        # Create a TCP socket (AF_INET=IPv4, SOCK_STREAM=TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # Try to complete TCP 3-way handshake
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            # connect_ex returns 0 on success = port is OPEN
            with lock:
                open_ports.append(port)
            service = KNOWN_PORTS.get(port, "Unknown Service")
            print(f" Port {port:<6} OPEN   → {service}")

    except socket.timeout:
        pass   # Filtered by firewall
    except Exception:
        pass   # Closed or unreachable

def scan_target(host, port_range=(1, 1024)):
    """Scan a range of ports using threads for speed"""

    print("=" * 58)
    print("   DAY 4 — TCP PORT SCANNER")
    print("=" * 58)
    print(f"\n  Target  : {host}")
    print(f"  Ports   : {port_range[0]} – {port_range[1]}")
    print(f"  Started : {datetime.now().strftime('%H:%M:%S')}")
    print(f"\n  Scanning... (open ports will appear below)\n")
    print("-" * 58)

    threads = []
    for port in range(port_range[0], port_range[1] + 1):
        t = threading.Thread(
            target=scan_port,
            args=(host, port)
        )
        threads.append(t)
        t.start()

        # Limit concurrent threads to avoid overwhelming system
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []

    # Wait for remaining threads
    for t in threads:
        t.join()

    print("-" * 58)
    print(f"\n  Scan Complete : {datetime.now().strftime('%H:%M:%S')}")
    print(f"  Open Ports    : {sorted(open_ports)}")

    if open_ports:
        print(f"\n  🔍 Security Analysis:")
        for port in sorted(open_ports):
            if port == 23:
                print(f"  Port 23 (Telnet) is DANGEROUS — sends passwords in plaintext!")
            if port == 21:
                print(f" Port 21 (FTP) — check if anonymous login is enabled")
            if port == 80:
                print(f" Port 80 (HTTP) — unencrypted, consider HTTPS only")
            if port == 3389:
                print(f"  Port 3389 (RDP) — common brute force target!")
            if port == 22:
                print(f" Port 22 (SSH) — encrypted, but check for weak passwords")

    print("=" * 58)

# ── Main ──────────────────────────────────────────────────
# Scan your own machine (localhost) — always safe and legal
# NEVER scan networks you don't own without permission
target = "127.0.0.1"   # localhost = your own PC

scan_target(target, port_range=(1, 1024))