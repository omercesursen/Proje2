import json


class OgrenciSistemi:
    def __init__(self):
        self.veritabani = {}
        self.verileri_yukle()

    def verileri_yukle(self):
        try:
            with open("ogrenciler.json", "r") as dosya:
                self.veritabani = json.load(dosya)
        except:
            self.veritabani = {}

    def verileri_kaydet(self):
        with open("ogrenciler.json", "w") as dosya:
            json.dump(self.veritabani, dosya)
        print("--- Veriler Dosyaya Kaydedildi! ---")

    def ekle(self):
        numara = input("Öğrenci No: ")
        if numara in self.veritabani:
            print("Bu numara zaten kayıtlı.")
            return

        ad = input("Ad: ")
        soyad = input("Soyad: ")
        notu = input("Not: ")

        self.veritabani[numara] = {"ad": ad, "soyad": soyad, "not": notu}
        print("Listeye eklendi (Kaydetmeyi unutma).")

    def listele(self):
        print("\n--- Öğrenci Listesi (JSON Formatlı) ---")
        if self.veritabani:
            print(json.dumps(self.veritabani, indent=4, ensure_ascii=False))
        else:
            print("Liste şu an boş.")

    def bul(self):
        numara = input("Aranacak No: ")
        if numara in self.veritabani:
            kisi = self.veritabani[numara]
            print(f"No: {numara} - Ad: {kisi['ad']} {kisi['soyad']} - Not: {kisi['not']}")
        else:
            print("Bulunamadı.")

    def sil(self):
        numara = input("Silinecek No: ")
        if numara in self.veritabani:
            del self.veritabani[numara]
            print("Listeden silindi (Kalıcı olması için Kaydet seç).")
        else:
            print("Bulunamadı.")

    def guncelle(self):
        numara = input("Güncellenecek No: ")
        if numara not in self.veritabani:
            print("Bulunamadı.")
            return

        eski = self.veritabani[numara]
        print("(Değiştirmek istemediğin yere Enter bas)")

        yeni_ad = input(f"Yeni Ad ({eski['ad']}): ")
        if yeni_ad != "":
            self.veritabani[numara]['ad'] = yeni_ad

        yeni_soyad = input(f"Yeni Soyad ({eski['soyad']}): ")
        if yeni_soyad != "":
            self.veritabani[numara]['soyad'] = yeni_soyad

        yeni_not = input(f"Yeni Not ({eski['not']}): ")
        if yeni_not != "":
            self.veritabani[numara]['not'] = yeni_not

        print("Güncellendi (Kaydetmeyi unutma).")


sistem = OgrenciSistemi()

while True:
    print("\n1-Ekle 2-Listele 3-Bul 4-Sil 5-Güncelle 6-KAYDET 7-Çıkış")
    secim = input("Seçim: ")

    if secim == "1":
        sistem.ekle()
        sistem.listele()
    elif secim == "2":
        sistem.listele()
    elif secim == "3":
        sistem.bul()
    elif secim == "4":
        sistem.sil()
        sistem.listele()
    elif secim == "5":
        sistem.guncelle()
        sistem.listele()
    elif secim == "6":
        sistem.verileri_kaydet()
    elif secim == "7":
        print("Çıkış yapılıyor...")
        break