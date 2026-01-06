# BLM101 Dönem Projesi
# Konu: Veri Depolama ve Sıkıştırma Algoritmaları – RLE (Run-Length Encoding)
# Öğrenci: Ayşe Nur Baştuğ
# Numara: 24360859041
# Açıklama: Bu program kullanıcıdan aldığı veriyi RLE yöntemi ile sıkıştırır (encode)
# ve geri açar (decode). Ayrıca sıkıştırma oranını (%) hesaplar.

def encode(data):
    """
    RLE Encode Fonksiyonu
    - Ardışık tekrar eden karakterleri sayar
    - '5A3B2C1D2A' gibi sıkıştırılmış veri döndürür
    """
    if not data:
        return ""
    
    result = ""
    count = 1
    prev_char = data[0]
    
    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            result += str(count) + prev_char
            prev_char = char
            count = 1
    
    # Son karakter grubunu ekle
    result += str(count) + prev_char
    return result
def encode(data):
    """
    RLE Encode Fonksiyonu
    - Ardışık tekrar eden karakterleri sayar
    - '5A3B2C1D2A' gibi sıkıştırılmış veri döndürür
    """
    if not data:
        return ""
    
    result = ""
    count = 1
    prev_char = data[0]
    
    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            result += str(count) + prev_char
            prev_char = char
            count = 1
    
    # Son karakter grubunu ekle
    result += str(count) + prev_char
    return result
def encode(data):
    """
    RLE Encode Fonksiyonu
    - Ardışık tekrar eden karakterleri sayar
    - '5A3B2C1D2A' gibi sıkıştırılmış veri döndürür
    """
    if not data:
        return ""
    
    result = ""
    count = 1
    prev_char = data[0]
    
    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            result += str(count) + prev_char
            prev_char = char
            count = 1
    
    # Son karakter grubunu ekle
    result += str(count) + prev_char
    return result
if __name__ == "__main__":
    # Kullanıcıdan girdi al
    user_input = input("Lütfen sıkıştırmak istediğiniz veriyi girin: ")
    
    # Encode
    encoded = encode(user_input)
    print("Encoded (Sıkıştırılmış) veri:", encoded)
    
    # Decode
    decoded = decode(encoded)
    print("Decoded (Orijinal) veri:", decoded)
    
    # Sıkıştırma oranı
    ratio = compression_ratio(user_input, encoded)
    print("Sıkıştırma Oranı: %", ratio)