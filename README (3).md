# Task 06 – Interpret an Ethernet Port Report

Given report: 100 Mb/s, half duplex, auto-negotiation off, 2,381 RX errors, 412 late collisions, 1,907 CRC errors.

Late collisions indicate a half-duplex collision detected after the first 512 bit times. CRC/FCS errors indicate corrupted frames. Together they suggest a duplex mismatch.

Linux example (run only on the correct interface and with permission):
```bash
sudo ethtool -s eth0 autoneg on
ethtool eth0
ethtool -S eth0
```
Windows: Device Manager → Network adapter → Properties → Advanced → Speed & Duplex → Auto Negotiation; ensure switch side is also auto.

`01:00:5e:0a:01:02` is an IPv4 multicast group MAC. `3c:52:82` is the OUI portion of the second address.

Jumbo frames can improve bulk CCTV storage efficiency, but every NIC, switch port and server on the path must support the same MTU. Do not mix jumbo frames with latency-critical robot traffic on a constrained link.

## Evidence you must capture
- [ ] Before-fix adapter/ethtool output
- [ ] After-fix output showing negotiated full duplex
- [ ] Counter comparison showing errors no longer increasing
