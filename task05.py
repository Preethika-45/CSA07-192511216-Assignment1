distance_m = 1200
speed_mps = 2
trip_s = distance_m / speed_mps
wifi_handoffs = distance_m / 30
fiveg_handoffs = distance_m / 300
wifi_outage_s = wifi_handoffs * 0.150
fiveg_outage_s = fiveg_handoffs * 0.020
sensor_load_kbps = 600 * 50 * 8 / 1000
gateway_kbps = 5
print(f"Trip time: {trip_s:.0f} s")
print(f"Wi-Fi handovers: {wifi_handoffs:.0f}; unavailable: {wifi_outage_s:.2f} s")
print(f"5G handovers: {fiveg_handoffs:.0f}; unavailable: {fiveg_outage_s:.2f} s")
print(f"LoRa sensor load: {sensor_load_kbps:.0f} kbps")
print(f"Gateway capacity: {gateway_kbps:.0f} kbps; overload factor: {sensor_load_kbps/gateway_kbps:.1f}x")
