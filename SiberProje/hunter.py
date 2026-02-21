import requests

hedef = "google.com"
kelimeler = ["www", "admin", "test", "dev", "api", "mail", "blog"]

print(f"--- {hedef} taraniyor ---")

for alt in kelimeler:
    url = f"http://{alt}.{hedef}"
    try:
        cevap = requests.get(url, timeout=2)
        if cevap.status_code == 200:
            sonuc = f"[+] {url} | Durum: {cevap.status_code}"
            print(sonuc)
            
            with open("bulunanlar.txt", "a") as dosya:
                dosya.write(sonuc + "\n")
                
    except requests.ConnectionError:
        pass
    except:
        pass

print("--- Tarama bitti. Sonuclar bulunanlar.txt dosyasina kaydedildi. ---")