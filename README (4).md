# Task 08 – Correct the Error or Ask Again?

For a 16-bit word, 2^r ≥ 16+r+1 gives r=5 check bits. Codeword length = 21 bits; check-bit overhead is 5/16 = 31.25% relative to data.

Code set {00000, 01011, 10101, 11110}: minimum Hamming distance = 3; detects up to 2 errors and corrects 1.

Received Hamming(7,4) word 0110111 has syndrome 5; flip bit 5 to recover 0110011 and data 1011.

At 40 ms retransmission delay, FEC is preferable for time-sensitive sensor traffic; ARQ may add unacceptable delay.

Run `python task08.py`.
