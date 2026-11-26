# Task 02 – Count the Domains in the Contractor's Drawing

## Required Packet Tracer topology
- 3 hubs, each with 8 PCs (24 PCs total)
- All three hubs connect to one 24-port switch
- That switch connects to router G0/0
- Router G0/1 connects to a second switch
- The second switch connects to 12 IP phones

## Expected domain counts (as analysed in the assignment)
- Collision domains: **17** (3 hub segments + 1 switch/router link + 1 router/second-switch link + 12 phone access links)
- Broadcast domains: **2** (the router separates the two sides)

## Device layers
- Hub: Layer 1
- Switch: Layer 2
- Router: Layer 3
- PC/IP phone: end devices use the full stack

## Connections
Hub segments are shared/multipoint. Individual Ethernet cables between end devices and hubs, switches, and router interfaces are physical point-to-point links.

## Standards
Ethernet IEEE 802.3 – IEEE; Wi-Fi IEEE 802.11 – IEEE; IPv4 RFC 791 – IETF; OSI ISO 7498 – ISO; 5G – 3GPP/ITU-R.

## Alternative: replace hubs with unmanaged switches
Collision domains become 41 using the assignment's counting method; broadcast domains remain 2. Per-port collision isolation improves, but unmanaged switches do not create VLAN separation or advanced QoS/security controls.

## Packet Tracer evidence to create yourself
1. Build and save `office.pkt` in this folder.
2. Take a screenshot showing all devices and links; save as `office_topology.png`.
3. Label the two broadcast domains and 17 collision domains in your report/diagram.
4. Open the `.pkt` file again to confirm it works.

**Not included:** a fabricated `.pkt` file. The topology must be built and verified in Packet Tracer.
