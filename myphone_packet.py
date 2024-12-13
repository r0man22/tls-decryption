import pyshark

target_ip = "192.168.1.26"

interface = "Wi-Fi"

capture = pyshark.LiveCapture(interface=interface)

print(f"Packet capturing is start")

try:
      for packet in capture.sniff_continuously():
          if "IP" in packet:
              src_ip = packet.ip.src
              dst_ip = packet.ip.dst

              if src_ip == target_ip or dst_ip == target_ip:
                  print(f"[{packet.sniff_time}] Packet details:\n{packet}")

except KeyboardInterrupt:
    print("\nPacket capturing stopped")
