# RLE (Run-Length Encoding) Sıkıştırıcı

## Öğrenci Bilgileri
- Ad: Ayşe Nur
- Soyad: Baştuğ
- Numara: 24360859041

## Proje Konusu
RLE (Run-Length Encoding) Sıkıştırıcı

## YouTube Linki
[Video Linki](Buraya_YouTube_Linki)

## Proje Açıklaması
Bu Python programı, verilen metin veya 0/1 matrisini Run-Length Encoding (RLE) yöntemiyle sıkıştırır ve eski hâline geri döndürür.

**Fonksiyonlar:**
- `encode(data)`: Girdiyi RLE ile sıkıştırır.
- `decode(data)`: Sıkıştırılmış veriyi eski hâline getirir.
- `compression_rate(original, compressed)`: Sıkıştırma oranını (%) hesaplar.

**Kullanım:**
1. Python dosyasını çalıştırın.
2. Kullanıcıdan veri girilmesini sağlayın (örn: "AAAAABBBCCDAA").
3. Program encode ve decode işlemlerini yapar, sıkıştırma oranını gösterir.

**Kütüphaneler:**  
- Python standart kütüphaneleri (ekstra kütüphane yok).

**Algoritma Mantığı:**  
- Encode: Ardışık tekrar eden karakterleri sayarak tek birim hâline getirir.  
- Decode: Sayı-karakter çiftlerini açarak orijinal veriyi geri üretir.