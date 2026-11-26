# Task 07 – Will the Receiver Notice the Error?

Generator: 1011 (x³+x+1). Data: 1101011011.
- Append three zeroes and divide using modulo-2 XOR.
- CRC remainder: **100**.
- Transmitted codeword: **1101011011100**.
- Received 1101011011101 has remainder 001 and is rejected.
- A degree-3 CRC detects every burst of length ≤3. Error patterns that are multiples of 1011 can be undetected (e.g. 1011).
- Internet checksum for 4500, 0073, 0000, 4000 is **7A8C**.

Run `python task07.py`.
