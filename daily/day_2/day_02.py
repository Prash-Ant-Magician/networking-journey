# Day 2 - OSI Layer Identifier
# Goal: Map real protocols and attacks to their OSI layers

# Dictionary of protocols mapped to OSI layers
OSI_LAYERS = {
    1: {
        "name": "Physical",
        "protocols": ["Ethernet (cable)", "WiFi (802.11)", "Fiber optic", "Bluetooth"],
        "devices":   ["Hub", "Cable", "Repeater"],
        "attacks":   ["Cable cutting", "Signal jamming", "USB drop attack"],
        "data_unit": "Bits"
    },
    2: {
        "name": "Data Link",
        "protocols": ["Ethernet", "ARP", "PPP", "MAC"],
        "devices":   ["Switch", "Bridge", "NIC"],
        "attacks":   ["MAC spoofing", "ARP poisoning", "VLAN hopping"],
        "data_unit": "Frame"
    },
    3: {
        "name": "Network",
        "protocols": ["IP", "ICMP", "OSPF", "BGP"],
        "devices":   ["Router", "Layer 3 Switch"],
        "attacks":   ["IP spoofing", "Ping of Death", "Route hijacking"],
        "data_unit": "Packet"
    },
    4: {
        "name": "Transport",
        "protocols": ["TCP", "UDP"],
        "devices":   ["Firewall", "Load Balancer"],
        "attacks":   ["SYN Flood", "UDP Flood", "Port scanning"],
        "data_unit": "Segment"
    },
    5: {
        "name": "Session",
        "protocols": ["NetBIOS", "PPTP", "RPC"],
        "devices":   ["Application gateway"],
        "attacks":   ["Session hijacking", "Session fixation"],
        "data_unit": "Data"
    },
    6: {
        "name": "Presentation",
        "protocols": ["SSL/TLS", "JPEG", "MPEG", "ASCII"],
        "devices":   ["Application gateway"],
        "attacks":   ["SSL stripping", "Format string attacks"],
        "data_unit": "Data"
    },
    7: {
        "name": "Application",
        "protocols": ["HTTP", "HTTPS", "FTP", "DNS", "SMTP", "SSH"],
        "devices":   ["Web server", "Email server", "DNS server"],
        "attacks":   ["SQL injection", "XSS", "Phishing", "DNS poisoning"],
        "data_unit": "Data"
    }
}

def display_layer(layer_num):
    """Display full details of a specific OSI layer"""
    if layer_num not in OSI_LAYERS:
        print("Invalid layer. Choose 1-7.")
        return

    layer = OSI_LAYERS[layer_num]
    print("\n" + "=" * 50)
    print(f"  LAYER {layer_num} — {layer['name'].upper()}")
    print("=" * 50)
    print(f"  Data Unit  : {layer['data_unit']}")
    print(f"  Protocols  : {', '.join(layer['protocols'])}")
    print(f"  Devices    : {', '.join(layer['devices'])}")
    print(f"  ⚠️  Attacks : {', '.join(layer['attacks'])}")
    print("=" * 50)

def display_all():
    """Display all 7 layers as a quick reference"""
    print("\n" + "=" * 60)
    print("        OSI MODEL — COMPLETE REFERENCE")
    print("=" * 60)
    print(f"  {'Layer':<8} {'Name':<15} {'Data Unit':<10} {'Key Protocol'}")
    print("-" * 60)
    for num in range(7, 0, -1):  # Top to bottom (7 to 1)
        layer = OSI_LAYERS[num]
        print(f"  {num:<8} {layer['name']:<15} {layer['data_unit']:<10} {layer['protocols'][0]}")
    print("=" * 60)

# ── Main Program ──────────────────────────────────
print("\n OSI LAYER REFERENCE TOOL — Day 2")
display_all()

print("\nDeep dive into a specific layer:")
print("   Enter a layer number (1-7) or 0 to exit\n")

while True:
    try:
        choice = int(input("Layer number: "))
        if choice == 0:
            print("\nStudy session complete.")
            break
        display_layer(choice)
    except ValueError:
        print("Please enter a number between 1 and 7")