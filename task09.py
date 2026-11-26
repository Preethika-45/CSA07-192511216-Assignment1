def required_window(rate_bps, rtt_s, frame_bytes):
    bdp_bits = rate_bps * rtt_s
    frames = bdp_bits / (frame_bytes * 8)
    return bdp_bits, frames

RATE = 1_000_000_000
RTT = 0.0126
FRAME_BYTES = 1500
bdp, frames = required_window(RATE, RTT, FRAME_BYTES)
print(f"Bandwidth-delay product: {bdp/8:.0f} bytes")
print(f"Frames in flight: {frames:.1f}")
print(f"Approximate integer window: {int(frames + 0.999999)} frames")
print("Note: apply the exact frame size and protocol assumptions specified by the assignment.")
