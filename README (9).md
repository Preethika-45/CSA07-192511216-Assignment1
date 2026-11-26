# Task 10 – Find Where the Delay Comes From

The assignment requires your own measurements, not copied/example values.

## Windows commands (PowerShell)
```powershell
ping -n 20 <destination>
tracert <destination>
```
Linux/macOS:
```bash
ping -c 20 <destination>
traceroute <destination>
```

Record destination, minimum/average/maximum RTT, packet loss and observations in `measurement_table.csv`. Capture your own traffic in Wireshark using display filter `icmp or tcp`; label Ethernet II, IPv4 and ICMP/TCP fields.

Do not fill measurement values until you run the tests on your own network.
