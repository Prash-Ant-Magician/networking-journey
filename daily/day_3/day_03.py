# Day 3 - ARP Table Reader & Network Mapper
# Goal: Read your real ARP table and understand MAC-to-IP mappings

import subprocess
import platform
import re

def get_arp_table():
    """Read the system ARP table"""
    system = platform.system().lower()

    if system == "windows":
        result = subprocess.run(["arp", "-a"],
                                capture_output=True, text=True)
    else:
        result = subprocess.run(["arp", "-n"],
                                capture_output=True, text=True)

    return result.stdout

def parse_arp_windows(raw_output):
    """Parse ARP output on Windows into structured data"""
    entries = []
    lines = raw_output.strip().split("\n")

    for line in lines:
        line = line.strip()
        # Match lines with IP and MAC pattern
        # Windows format: 192.168.1.1    aa-bb-cc-dd-ee-ff    dynamic
        match = re.match(
            r"(\d+\.\d+\.\d+\.\d+)\s+([\w\-]+)\s+(\w+)", line
        )
        if match:
            ip, mac, arp_type = match.groups()
            entries.append({
                "ip"  : ip,
                "mac" : mac.upper(),
                "type": arp_type
            })
    return entries

def identify_device_type(ip, mac):
    """Guess device type from IP and MAC patterns"""

    # Common router IPs
    if ip.endswith(".1") or ip.endswith(".254"):
        role = "Router/Gateway"
    elif mac.startswith("FF-FF-FF"):
        role = "Broadcast"
    else:
        role = "End Device"

    # Known manufacturer OUIs (first 3 bytes of MAC)
    oui = mac[:8].upper()
    manufacturers = {
        "00-50-56": "VMware (Virtual Machine)",
        "00-0C-29": "VMware (Virtual Machine)",
        "00-1A-A0": "Dell",
        "3C-22-FB": "Apple",
        "00-D0-BC": "Cisco",
        "B4-2E-99": "Cisco",
        "DC-A6-32": "Raspberry Pi",
        "00-15-5D": "Microsoft (Hyper-V)",
    }
    vendor = manufacturers.get(oui, "Unknown Vendor")

    return role, vendor

def display_arp_table(entries):
    """Display ARP table in a clean, informative format"""

    if not entries:
        print("  ⚠️  No ARP entries found.")
        print("  Try: ping your router first, then run again.")
        return

    print(f"\n  {'IP Address':<18} {'MAC Address':<22} {'Type':<10} {'Role':<25} {'Vendor'}")
    print("  " + "-" * 95)

    for entry in entries:
        role, vendor = identify_device_type(entry["ip"], entry["mac"])
        print(f"  {entry['ip']:<18} {entry['mac']:<22} "
              f"{entry['type']:<10} {role:<25} {vendor}")

def explain_mac(mac):
    """Break down a MAC address"""
    mac_clean = mac.replace("-", ":").replace(".", ":")
    parts = mac_clean.split(":")
    if len(parts) >= 3:
        oui = ":".join(parts[:3]).upper()
        device_id = ":".join(parts[3:]).upper()
        print(f"\n  MAC Breakdown: {mac_clean.upper()}")
        print(f"  OUI (Manufacturer ID) : {oui}")
        print(f"  Device ID             : {device_id}")

# ── Main ──────────────────────────────────────────
print("=" * 55)
print("   DAY 3 — ARP TABLE READER & NETWORK MAPPER")
print("=" * 55)

print("\n📡 Reading your ARP table...")
raw = get_arp_table()

print("\nDevices Currently Known to Your System:")
entries = parse_arp_windows(raw)
display_arp_table(entries)

# Show first entry MAC breakdown
if entries:
    print("\nMAC Address Breakdown (first entry):")
    explain_mac(entries[0]["mac"])

print("\n ARP Facts:")
print("  → ARP maps IP addresses to MAC addresses")
print("  → ARP cache is temporary (entries expire)")
print("  → FF:FF:FF:FF:FF:FF = broadcast (sent to everyone)")
print("  → ARP has NO authentication = vulnerable to poisoning")
print("  → Attacker can fake ARP replies = Man-in-the-Middle")

print("\n" + "=" * 55)
print("  Run: arp -a   in CMD to see raw table anytime")
print("=" * 55)