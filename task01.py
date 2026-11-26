robot_mbps = 40 * (200 * 8) / 0.002 / 1_000_000
sensor_mbps = 600 * 50 * 8 / 1_000_000
cctv_mbps = 24 * 4
office_mbps = 150 * 0.10 * 2

line = robot_mbps + sensor_mbps + cctv_mbps + office_mbps
plant = 8 * line
motion_cctv = cctv_mbps * 0.05
motion_line = robot_mbps + sensor_mbps + motion_cctv + office_mbps

print(f"Robots: {robot_mbps:.2f} Mbps")
print(f"Sensors: {sensor_mbps:.2f} Mbps")
print(f"CCTV: {cctv_mbps:.2f} Mbps")
print(f"Office: {office_mbps:.2f} Mbps")
print(f"One line: {line:.2f} Mbps")
print(f"Eight lines: {plant:.2f} Mbps")
print(f"Motion-triggered CCTV: {motion_cctv:.2f} Mbps")
print(f"Revised line: {motion_line:.2f} Mbps")
print(f"Revised plant: {8 * motion_line:.2f} Mbps")
