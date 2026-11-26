# Task 11 – Defend the Network Design

## Recommended design summary
- Robot cell near welders: shielded Cat6A S/FTP or fibre, full duplex, dedicated VLAN and strict priority.
- Office-to-shop-floor 140 m: multimode fibre.
- Shop-floor-to-data-centre 550 m: single-mode fibre.
- CCTV: wired/fibre, separate VLAN, shaped traffic; jumbo MTU only on an end-to-end compatible storage path.
- Offices/handhelds: Wi-Fi 6 with 802.11r and WPA3.
- Sensors: wired/Wi-Fi/5G mMTC depending on rate; LoRa only for very low-rate sensors.
- Plant-to-head-office: carrier WAN with diverse backup; keep robot control local.

## Key numeric reasons
- Eight-line traffic: 1.266 Gbps > 1 Gbps uplink.
- Motion-triggered CCTV alternative: 536.32 Mbps for eight lines.
- 140 m and 550 m links exceed copper Ethernet distance.
- Wi-Fi roaming outage is much larger than private 5G in the given assumptions.
- Duplex mismatch indicators include late collisions and CRC errors.

## Risks
1. WAN single point of failure and variable delay.
2. Welding EMI and congestion at shared uplinks.

For five plants, route and aggregate traffic at Layer 3, retain local robot/CCTV traffic, and size WAN/head-office aggregation from measured flows. Update this defence with the measurements you obtain in Task 10.
