import requests
import sys

if len(sys.argv) < 2:
    print("Kullanim: python hunter.py hedefsite.com")
    sys.exit()

hedef = sys.argv[1]
wordlist_dosyasi = "wordlist.txt"
bulunan_sayisi = 0

print(f"--- {hedef} taraniyor ---")

try:
    with open(wordlist_dosyasi, "r") as dosya:
        for satir in dosya:
            alt = satir.strip()
            if not alt:
                continue
                
            url = f"http://{alt}.{hedef}"
            try:
                cevap = requests.get(url, timeout=2)
                if cevap.status_code == 200:
                    sonuc = f"[+] {url} | Durum: {cevap.status_code}"
                    print(sonuc)
                    
                    with open("bulunanlar.txt", "a", encoding="utf-8") as f:
                        f.write(sonuc + "\n")
                    bulunan_sayisi += 1
            except:
                pass

except FileNotFoundError:
    print(f"Hata: {wordlist_dosyasi} bulunamadi!")

print(f"--- Tarama bitti. Toplam {bulunan_sayisi} subdomain kaydedildi. ---")
