def mod2_div(dividend, divisor):
    rem = list(dividend)
    for i in range(len(dividend) - len(divisor) + 1):
        if rem[i] == "1":
            for j in range(len(divisor)):
                rem[i + j] = "0" if rem[i + j] == divisor[j] else "1"
    return "".join(rem[-(len(divisor) - 1):])

def encode(data, gen):
    return data + mod2_div(data + "0" * (len(gen)-1), gen)

def check(frame, gen):
    return set(mod2_div(frame, gen)) == {"0"}

def internet_checksum(words):
    total = sum(int(w, 16) for w in words)
    while total >> 16:
        total = (total & 0xffff) + (total >> 16)
    return f"{(~total) & 0xffff:04x}"

if __name__ == "__main__":
    gen = "1011"
    frame = encode("1101011011", gen)
    print("transmitted:", frame)
    print("no error :", check(frame, gen))
    bad = frame[:-1] + ("1" if frame[-1] == "0" else "0")
    print("1-bit error:", check(bad, gen))
    burst = frame[:2] + "".join("1" if b == "0" else "0" for b in frame[2:5]) + frame[5:]
    print("3-bit burst:", check(burst, gen))
    for pattern in ("1011", "11101"):
        altered = frame[:-len(pattern)] + "".join("1" if b == "0" else "0" for b in frame[-len(pattern):])
        print("illustrative pattern", pattern, "is a multiple of generator:", mod2_div(pattern, gen) == "000")
    print("checksum:", internet_checksum(["4500", "0073", "0000", "4000"]))
