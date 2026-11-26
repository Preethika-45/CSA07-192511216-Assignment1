# Task 03 – Read a Captured Frame Layer by Layer

## Capture interpretation
- Ethernet II: OSI Layer 2, frame; EtherType 0x0800 means IPv4.
- IPv4: Layer 3, packet; source 10.10.1.25, destination 10.10.9.4, TTL 61.
- TCP: Layer 4, segment; source port 51522, destination port 502 (Modbus/TCP), payload 12 bytes.
- Modbus command: application data (upper OSI layers).
- Routers crossed: 64 − 61 = **3**.
- Robot command frame: 12 + 20 TCP + 20 IPv4 + 14 Ethernet + 4 FCS = **70 bytes**; overhead 58/70 = **82.9%**.
- Camera packet: 1,400 + 20 + 20 + 14 + 4 = **1,458 bytes**; overhead 58/1,458 = **3.98%**.

Fault mapping: wrong MAC → Layer 2; TTL expiry → Layer 3; closed TCP port → Layer 4.

## Alternative: raw Ethernet
Removing IP and TCP headers nominally saves 40 bytes, but minimum Ethernet frame padding means the practical frame reduction for a 12-byte payload is only 6 bytes (70 to 64 bytes). Losses include IP routing, TTL, TCP reliability/flow control, IP/port firewalling and standard IP diagnostic tools.

## Run
`python task03.py`

## Evidence
- [ ] Create your own Wireshark capture (`task03_capture.pcapng`)
- [ ] Label Ethernet II, IPv4, TCP and Modbus/data fields in a screenshot
- [ ] Save screenshot as `task03_wireshark.png`
