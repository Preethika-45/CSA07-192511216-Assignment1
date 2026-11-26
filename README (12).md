# Task 01 – Size the Traffic Before Choosing Anything

## Given traffic and calculations
- Robots: 40 × (200 bytes × 8 bits/byte ÷ 0.002 s) = **32.00 Mbps**
- Vibration sensors: 600 × 50 bytes/s × 8 = **0.24 Mbps**
- CCTV: 24 × 4 Mbps = **96.00 Mbps**
- Office: 150 × 10% × 2 Mbps = **30.00 Mbps**
- One line: 32 + 0.24 + 96 + 30 = **158.24 Mbps**
- Eight lines: 8 × 158.24 = **1,265.92 Mbps ≈ 1.27 Gbps**

CCTV is the largest source. Robot control has the strictest deadline (10 ms); they are not the same source. A 1 Gbps uplink is insufficient for eight lines (126.6% offered load). Use separate VLANs/queues, strict priority for robot control, CCTV shaping, and a 10 Gbps backbone.

## 100 ms delay ranking
1. Robot control – ten times the 10 ms deadline.
2. Vibration alarms – may delay urgent event detection.
3. CCTV – buffering can absorb some fixed delay; jitter/loss matter.
4. Office/ERP/email – least time-sensitive.

## Alternative: motion-triggered CCTV at 5%
CCTV = 96 × 0.05 = 4.8 Mbps. Revised line = **67.04 Mbps**; eight lines = **536.32 Mbps** (53.6% of 1 Gbps). The average load fits, but bursts and live-view limitations remain.

## Run
`python task01.py`

## Evidence
- [ ] Save terminal output as `task01_output.txt`
- [ ] Add a screenshot of the output
- [ ] Commit your work
