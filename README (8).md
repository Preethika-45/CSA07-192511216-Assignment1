# Task 12 – Re-evaluate and Adapt the Design

## Assumed AGV traffic (assignment assumption)
Per AGV: 200-byte command every 10 ms = 0.16 Mbps; 200-byte telemetry every 10 ms = 0.16 Mbps; obstacle camera = 4 Mbps. Total = 4.32 Mbps per AGV. For 50 AGVs = **216 Mbps**.

Plant traffic with AGVs: 1,265.92 + 216 = **1,481.92 Mbps**. A 1 Gbps uplink is 148.2% loaded; a 10 Gbps backbone is 14.8% loaded.

## Test of original design
Wi-Fi: about 40 handovers × 150 ms = 6 s unreachable per 600 s trip. With assumed 802.11r 30 ms, 1.2 s unreachable. Both fail a strict zero-missed-command requirement.

## Revised design
Decision: **MODIFY**.
- Retain fixed robot wired links, CCTV cable/fibre, office Wi-Fi and WAN.
- Use private 5G URLLC for mobile AGVs with overlapping cells, dual connectivity/conditional handover and an onboard watchdog.
- Use mMTC for suitable sensors.
- Upgrade backbone to 10 Gbps fibre with resilient ring/core.
- Use radio FEC/HARQ; Ethernet CRC-32; suitable WAN sliding-window transport.

## Evidence to create yourself
- [ ] Build revised topology in Packet Tracer where supported; save `revised.pkt`
- [ ] Save screenshot `revised_topology.png`
- [ ] Document any 5G elements Packet Tracer cannot model; do not pretend a Packet Tracer 5G simulation exists if your version lacks it.
- [ ] Update this README with your actual simulation steps and results.
