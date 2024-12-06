from scapy.all import sniff

def packet_capturer(packet):
	if packet.haslayer('TCP') and packet['TCP'].dport == 443:
		print(packet.show())

sniff(prn=packet_capturer, filter="tcp port 443")
