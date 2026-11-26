# Task 05 – Wi-Fi 6 or 5G for Moving Equipment?

Trip distance 1,200 m at 2 m/s = 600 s.
- Wi-Fi: 30 m spacing → approximately 40 handovers; 40 × 150 ms = **6.0 s** unreachable.
- Private 5G: 300 m coverage → approximately 4 handovers; 4 × 20 ms = **0.08 s** unreachable.
- AGVs/robot control: URLLC; CCTV: eMBB; many low-rate sensors: mMTC.
- Bluetooth LE: nearby personal peripherals/tools; Zigbee: low-rate local sensor/actuator mesh; LoRaWAN: sparse, very low-rate long-range sensors.
- 802.11r can reduce roaming time, but contention, interference and client roaming behaviour still make deterministic 10 ms guarantees difficult.

LoRa alternative: 600 × 50 B/s × 8 = **240 kbps**, much greater than one assumed 5 kbps gateway capacity. These vibration sensors cannot all fit on one gateway at that rate.

Run `python task05.py`.
