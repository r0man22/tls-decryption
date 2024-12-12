
import pyshark

# Ethernet bağlantınızı kullanın (genellikle eth0)
capture = pyshark.LiveCapture(interface='Ethernet', display_filter='(http.request.method == "GET" or http.request.method == "POST") or ssl.handshake')
try:
    for packet in capture.sniff_continuously():
        protocol = packet.transport_layer
        src_ip = packet.ip.src
        dest_ip = packet.ip.dst
        src_port = packet[packet.transport_layer].srcport
        dest_port = packet[packet.transport_layer].dstport

        print(f"Protocol : {protocol}, Src IP: {src_ip}, Dst IP: {dest_ip}, Src Port: {src_port}, Dest Port: {dest_port}")

except KeyboardInterrupt:
    print("Paket capturing processing stopped.")

except Exception as e:
    print(f"Something wrong: {e}")

