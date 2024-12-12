import pyshark
import asyncio

# Paket yakalamayı başlatıyoruz
c.apture = pyshark.LiveCapture(interface='eth0', display_filter = 'tls.handshake.extensions_server_name or tls.handshake or http.request')

# Paket yakalama işlemini dosyaya yazma
try:
    with open("captured.txt", "w") as file:
        loop = asyncio.get_event_loop()
        for packet in capture.sniff_continuously():
            file.write(str(packet) + "\n")
            
except KeyboardInterrupt:
    print("Paket yakalama işlemi durduruldu.")

except EOFError:
    print("EOFError: Akış sona erdi.")

finally:
    # Asyncio olay döngüsünü düzgün bir şekilde kapatıyoruz
    loop.close()

