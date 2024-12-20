import pyshark

interface = 'eth0"

capture = pyshark.LiveCapture(interface=interface, display_filter="tls and frame matches 'Application Data'")

for packet in capture.sniff_continuously():
	try:
		if hasattr(packet, 'tls') and hasattr(packet.tls, 'app_data'):
			app_data = packet.tls.app_data
			print(f"Packet Number: {packet.number}")
			print(f"Timestamp: {packet.sniff_time}")
			print(f"Source IP: {packet.ip.src}")
			print(f"Destination IP: {packet.ip.dst}")
			print(f"Encrypted Application Data (hex): {app_data}")
			print("-" * 50)
	except AttributeError:
		print("TLS Application Data is not available")
