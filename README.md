# 🛡️ Networking & Cybersecurity Journey
### 365 Days | Zero to Professional | By Prash

[![Days Completed](https://img.shields.io/badge/Days%20Completed-4%2F365-00ff88?style=for-the-badge&logo=target&logoColor=black)](.)
[![Current Phase](https://img.shields.io/badge/Phase-Foundations-0099ff?style=for-the-badge)](.)
[![Tools](https://img.shields.io/badge/Tools-Packet%20Tracer%20%7C%20Python%20%7C%20Wireshark-ff6600?style=for-the-badge)](.)
[![OS](https://img.shields.io/badge/OS-Windows-0078D4?style=for-the-badge&logo=windows)](.)
[![Goal](https://img.shields.io/badge/Goal-Cybersecurity%20Professional-red?style=for-the-badge)](.)

---

## 👤 About This Repository

This is my **public learning portfolio** documenting a structured 365-day journey from zero networking knowledge to professional-level cybersecurity skills.

Every day I:
- Learn a core networking or security concept
- Build something practical in **Cisco Packet Tracer**
- Write a **Python tool** that applies the concept
- Run experiments (including breaking things on purpose)
- Push everything here as proof of work

> *"Every layer you learn is one more layer of attacks you can understand and defend."*

---

## 🗺️ The Roadmap

```
PHASE 1 — FOUNDATIONS          [Days 00–30]   ← YOU ARE HERE
PHASE 2 — PROTOCOLS DEEP DIVE  [Days 31–90]
PHASE 3 — SECURITY CONCEPTS    [Days 91–180]
PHASE 4 — OFFENSIVE SECURITY   [Days 181–270]
PHASE 5 — DEFENSIVE SECURITY   [Days 271–330]
PHASE 6 — CAPSTONE PROJECTS    [Days 331–365]
```

---

## 📅 Daily Log

### ✅ PHASE 1 — FOUNDATIONS

---

#### 🗓️ Day 0 — Lab Setup & First Recon
**Date:** Day 0  
**Status:** ✅ Complete

**What I learned:**
- Installed the full cybersecurity lab: Python, Cisco Packet Tracer, VS Code, GitHub
- Ran first real reconnaissance commands: `ipconfig`, `ping`, `tracert`
- Traced my packets all the way to Google's Delhi datacenter (12 hops, IPv6)
- Understood that `tracert` is the same tool hackers use for network reconnaissance

**Key insight:**
> The `* * * Request timed out` hops in traceroute are routers hardened against probing — my first real-world example of network defense.

**Files:**
- [`day00_setup_check.py`](./day00_setup_check.py) — System verification script

**Concepts:** Reconnaissance · IPv4 vs IPv6 · Latency · Network Hops

---

#### 🗓️ Day 1 — IP Addressing & First Network
**Date:** Day 1  
**Status:** ✅ Complete

**What I learned:**
- Private vs Public IP addresses and why the distinction matters
- Built my **first 2-PC network in Packet Tracer** — two computers talking to each other
- Discovered my real network: `10.129.226.0/24` (institutional/corporate range)
- Ran 3 deliberate failure experiments to understand what breaks networks

**Experiments & Results:**
| Experiment | What I Did | What Broke | Why |
|---|---|---|---|
| 1 | Changed PC1 to wrong subnet | 100% packet loss | Different networks need a router |
| 2 | Set both PCs to same IP | Inconsistent replies | IP conflict — two devices can't share one address |
| 3 | Deleted the cable | 100% packet loss | Physical layer is the foundation |

**Key insight:**
> My IP starts with `10.x.x.x` — that's a corporate/institutional range. Real-world networking, not just a home lab.

**Files:**
- [`day01_network_scanner.py`](./day01_network_scanner.py) — Network discovery tool using Python sockets

**Concepts:** IPv4 Addressing · Private/Public IPs · Subnetting · NAT · Default Gateway · Socket Programming

---

#### 🗓️ Day 2 — The OSI Model
**Date:** Day 2  
**Status:** ✅ Complete

**What I learned:**
- All 7 OSI layers with their protocols, devices, and associated attacks
- Watched real packets move through OSI layers in Packet Tracer simulation mode
- Mapped every cyberattack I know to its OSI layer
- Understood encapsulation: how each layer wraps data like an onion

**OSI Attack Map:**
| Layer | Name | Key Attack |
|---|---|---|
| 7 | Application | SQL Injection, XSS, Phishing |
| 6 | Presentation | SSL Stripping |
| 5 | Session | Session Hijacking |
| 4 | Transport | SYN Flood, Port Scanning |
| 3 | Network | IP Spoofing, Route Hijacking |
| 2 | Data Link | ARP Poisoning, MAC Spoofing |
| 1 | Physical | Cable cutting, Signal jamming |

**Key insight:**
> When I pinged in Packet Tracer, Layers 4–7 were completely empty. Ping (ICMP) only uses Layers 1–3. Higher layers only activate when applications are involved.

**Files:**
- [`day02_osi_identifier.py`](./day02_osi_identifier.py) — Interactive OSI layer reference tool

**Concepts:** OSI Model · Encapsulation · TCP vs UDP · ICMP · Protocol Stack

---

#### 🗓️ Day 3 — MAC Addresses, ARP & Switch Behavior
**Date:** Day 3  
**Status:** ✅ Complete

**What I learned:**
- How ARP resolves IP → MAC addresses (the missing piece between Layer 2 and Layer 3)
- Read and decoded my real ARP table — found my router's MAC: `00:60:47:A1:0E:42` (Cisco OUI)
- How switches build their MAC table by learning from traffic
- Why ARP has zero authentication — and why that's a serious vulnerability

**ARP Process:**
```
PC0 needs to send to 192.168.1.2 but doesn't know its MAC

1. Check ARP cache → not found
2. Broadcast: "Who has 192.168.1.2?" → FF:FF:FF:FF:FF:FF
3. PC1 replies: "That's me — MAC: 00:60:47:A1:0E:42"
4. Cache the result
5. Build the frame and send
```

**Security finding:**
> ARP has NO authentication. Anyone can send a fake ARP reply ("I am the router"). This is ARP Poisoning — the foundation of Man-in-the-Middle attacks. My home network has zero protection against this.

**Files:**
- [`day03_arp_mapper.py`](./day03_arp_mapper.py) — ARP table reader with MAC OUI identification

**Concepts:** ARP Protocol · MAC Addresses · OUI · Switch MAC Table · CAM Overflow · ARP Poisoning · Gratuitous ARP · MITM

---

#### 🗓️ Day 4 — TCP/IP, Ports & The Three-Way Handshake
**Date:** Day 4  
**Status:** ✅ Complete

**What I learned:**
- TCP's 3-way handshake (SYN → SYN-ACK → ACK) and why it exists
- How SYN Flood attacks exploit the handshake to exhaust server memory
- Port numbers: what they are, why they matter, which ones are dangerous
- Built a real TCP port scanner from scratch using Python threading

**Key Ports (Memorized):**
```
22  = SSH      80  = HTTP     443 = HTTPS
23  = Telnet   53  = DNS      445 = SMB
21  = FTP      25  = SMTP    3389 = RDP
```

**Port Scanner Architecture:**
```python
# Core logic: attempt TCP 3-way handshake
sock.connect_ex((host, port))
# Returns 0 = handshake succeeded = port OPEN
# Returns error = port CLOSED or FILTERED
```

**Key insight:**
> Port 23 (Telnet) open on any modern system = critical finding. Sends usernames and passwords in plaintext. Any attacker on the same network can capture credentials with Wireshark.

**Files:**
- [`day04_port_scanner.py`](./day04_port_scanner.py) — Multithreaded TCP port scanner

**Concepts:** TCP · UDP · Three-Way Handshake · SYN Flood · Ports · Port Scanning · Threading · DoS Attacks

---

## 🧰 Tools & Environment

| Tool | Purpose | Status |
|---|---|---|
| Cisco Packet Tracer | Network simulation & visualization | ✅ Installed |
| Python 3.x | Scripting & tool development | ✅ Installed |
| VS Code | Code editor | ✅ Installed |
| Wireshark | Packet capture & analysis | 🔜 Day 10 |
| Nmap | Network scanning | 🔜 Day 15 |
| Metasploit | Penetration testing framework | 🔜 Day 90 |
| Kali Linux | Security-focused OS | 🔜 Day 60 |

---

## 🐍 Python Tools Built

| File | Day | What It Does |
|---|---|---|
| `day00_setup_check.py` | 0 | Verifies lab environment and prints system info |
| `day01_network_scanner.py` | 1 | Discovers local IP, network range, and tests connectivity |
| `day02_osi_identifier.py` | 2 | Interactive OSI layer reference with attack mappings |
| `day03_arp_mapper.py` | 3 | Reads ARP table and identifies device manufacturers via OUI |
| `day04_port_scanner.py` | 4 | Multithreaded TCP port scanner with security analysis |

---

## 📡 My Lab Environment

```
Network    : 10.129.226.0/24
My IP      : 10.129.226.x
Router     : 10.129.226.1  (MAC: 00:60:47:A1:0E:42 — Cisco)
Router OUI : 00:60:47 = Cisco Systems
DNS Used   : 8.8.8.8 (Google), 1.1.1.1 (Cloudflare)
Internet   : IPv6 enabled (2404:xxxx range — Jio/Airtel)
Hops to Google : 12 hops → Google Delhi Datacenter
                 (tzdelb-at-in-x0e.1e100.net)
OS         : Windows
```

---

## 🧠 Concepts Mastered

```
✅ IP Addressing (Private/Public/IPv4/IPv6)
✅ Subnetting basics (255.255.255.0 / /24 notation)
✅ OSI 7-Layer Model (all layers + attacks per layer)
✅ Encapsulation & Decapsulation
✅ ARP Protocol (request, reply, cache, poisoning)
✅ MAC Addresses (structure, OUI, spoofing)
✅ Switch MAC Table (learning, flooding, overflow)
✅ TCP 3-Way Handshake (SYN, SYN-ACK, ACK)
✅ TCP vs UDP (use cases, differences)
✅ Port Numbers (well-known ports, scanning)
✅ ICMP (ping, traceroute, types)
✅ SYN Flood Attack (how it works, why it's effective)
✅ ARP Poisoning (Gratuitous ARP, MITM setup)
✅ Port Scanning (open/closed/filtered states)
✅ Python socket programming
✅ Python subprocess & threading
```

---

## ⚔️ Attacks Studied (Theory)

| Attack | Layer | Status |
|---|---|---|
| ARP Poisoning / MITM | Layer 2 | ✅ Studied |
| MAC Flooding (CAM overflow) | Layer 2 | ✅ Studied |
| MAC Spoofing | Layer 2 | ✅ Studied |
| IP Spoofing | Layer 3 | ✅ Studied |
| SYN Flood (DoS) | Layer 4 | ✅ Studied |
| Port Scanning | Layer 4 | ✅ Studied |
| Session Hijacking | Layer 5 | ✅ Studied |
| SSL Stripping | Layer 6 | ✅ Studied |
| Phishing | Layer 7 | ✅ Studied |
| SQL Injection | Layer 7 | ✅ Studied |
| Gratuitous ARP attack | Layer 2 | ✅ Studied |
| DNS Poisoning | Layer 7 | 🔜 Upcoming |
| VLAN Hopping | Layer 2 | 🔜 Upcoming |
| BGP Hijacking | Layer 3 | 🔜 Upcoming |

---

## 📈 Progress Stats

```
Days Completed    :  4 / 365  (1.1%)
Python Files Built:  5
PT Labs Completed :  4
Attacks Studied   : 11
Concepts Learned  : 15+
Experiments Run   :  9
Streak            :  4 days 🔥
```

---

## 📚 Resources I'm Using

- Cisco Networking Academy — Packet Tracer
- Python Docs — `socket`, `subprocess`, `threading`
- RFC 826 — ARP Specification (original)
- RFC 793 — TCP Specification (original)

---

## ⚠️ Ethics Notice

All tools in this repository are built for **educational purposes only**.  
All scanning and testing is performed exclusively on:
- My own machines (`127.0.0.1`)
- My own lab networks
- Packet Tracer simulations

Scanning or attacking systems without explicit written permission is **illegal**.  
This repository documents learning, not exploitation.

---

## 🎯 Next Milestones

- [ ] Day 5 — DNS: How names become IP addresses
- [ ] Day 8 — ARP Poisoning lab (ethical, controlled)
- [ ] Day 10 — Wireshark: capture and analyze real packets
- [ ] Day 15 — Nmap: professional port scanning
- [ ] Day 30 — Phase 1 complete: full network built in Packet Tracer
- [ ] Day 60 — First Kali Linux setup
- [ ] Day 90 — First CTF challenge attempt

---

*Updated daily. Last update: Day 4.*