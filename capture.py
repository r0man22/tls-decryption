import pyshark
import asyncio

# Paket yakalamayı başlatıyoruz
capture = pyshark.LiveCapture(interface='eth0', display_filter = 'tls.record.version == 0x0303 or tls.record.version == 0x0304')

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

