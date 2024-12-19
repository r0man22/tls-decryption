import pyshark

pcap_file = 'tls.pcapng'

capture = pyshark.FileCapture(pcap_file, display_filter='tls and info contains "application data"')

for packet in capture:
	print(f"Packet Number: {packet.number}")
	print(f"Timestamp: {packet.sniff_time}")

	if hasattr(packet, 'tls') and hasattr(packet.tls, 'record_version'):
		if '1.2' in str(packet.tls.record_version):
			protocol = 'TLSv1.2'
		elif '1.3' in str(packet.tls.record_version):
			protocol = 'TLSv1.3'
		else:
			protocol = 'Unknown TLS Version'
		print(f"Protocol: {protocol}")
	else:
		print("Protocol: Not TLS")
	
	print(f"Length: {packet.length} bytes")

	print(f"Info: {packet.tls._all_fields.get('tls.record_info', 'N/A')}")

	print("Layers:")
	for layer in packet.layers:
		print(f"  - {layer.layer_name}")
	print("-" * 50)

capture.close()
