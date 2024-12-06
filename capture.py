import pyshark

capture = pyshark.LiveCapture(interface='eth0', display_filter='tcp.port == 443')

try:
    with open("captured.txt", "w") as file:
        for packet in capture.sniff_continuously():
            file.write(str(packet) + "\n")
except KeyboardInterrupt:
    print("Paket yakalama işlemi durduruldu.")
except EOFError:
    print("Akış sona erdi.")

