# Task 04 – Choose a Medium for Each Run

## Medium decisions
- Robot cell near welders, 85 m: Cat6A S/FTP with correct bonding; fibre if routed beside welding cables. Shielding/fibre mitigates EMI.
- Office to shop-floor switch, 140 m: multimode fibre; exceeds 100 m copper Ethernet channel limit.
- Shop floor to data centre, 550 m: single-mode OS2 fibre gives distance and growth margin.
- Plant to head office, 400 km: carrier leased line / carrier Ethernet / MPLS over fibre, with a diverse backup.

Runs b, c and d exceed 100 m copper Ethernet. Run a is within distance but ordinary UTP is vulnerable to welding EMI.

Shannon capacity C = B log2(1+SNR):
- 250 MHz at 40 dB: about **3,322 Mbps**
- 250 MHz at 15 dB: about **1,257 Mbps**
- Wi-Fi 6, 160 MHz at 15 dB: about **804 Mbps** (theoretical; delay/jitter is the concern for robot control).

## Run
`python task04.py`
