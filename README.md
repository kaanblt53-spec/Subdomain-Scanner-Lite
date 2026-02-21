# Simple Subdomain Hunter
Python ile ilk siber güvenlik projem.
Bu araç, bir kelime listesi (`wordlist.txt`) kullanarak hedef web sitesine ait aktif subdomainleri (alt alan adlarını) tespit eder.

## 🚀 Özellikler
- **Wordlist Desteği:** Aramaları bir metin dosyasından okur.
- **Raporlama:** Bulunan sonuçları `bulunanlar.txt` dosyasına kaydeder.
- **Dinamik Hedef:** Komut satırı üzerinden her site taranabilir.

## 🛠️ Kullanım
1. `wordlist.txt` dosyanızın içine taramak istediğiniz kelimeleri ekleyin.
2. Terminale şu komutu yazın:
```bash
python hunter.py hedefsite.com
