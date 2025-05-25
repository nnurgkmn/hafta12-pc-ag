import socket

# Sunucunun IP ve port bilgisi
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

# UDP soketi oluşturuluyor
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Soket IP ve port'a bağlanıyor
UDPServerSocket.bind((localIP, localPort))
print("UDP sunucu başlatıldı ve dinleniyor...")

# Kullanıcı adı - şifre sözlüğü (veritabanı gibi düşünebilirsin)
kullanicilar = {
    '17BIT0382': 'vivek',
    '17BEC0647': 'shikhar',
    '17BEC0150': 'tanveer',
    '17BCE2119': 'sahil',
    '17BIT0123': 'sidhant'
}

# Sürekli dinleme döngüsü
while True:
    # Kullanıcı adını al
    name_bytes, addr = UDPServerSocket.recvfrom(bufferSize)
    name = name_bytes.decode("utf-8")

    # Şifreyi al
    pwd_bytes, _ = UDPServerSocket.recvfrom(bufferSize)
    pwd = pwd_bytes.decode("utf-8")

    # Giriş kontrolü
    if name not in kullanicilar:
        msg = "listede böyle bir isim yok"
    elif kullanicilar[name] == pwd:
        msg = "giriş başarılı"
    else:
        msg = "şifre hatalı"

    # Cevap gönder
    UDPServerSocket.sendto(msg.encode("utf-8"), addr)
