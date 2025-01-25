ogrenciler = {
    "Ali": [85, 90, 78],
    "Zehra": [92, 88, 95],
    "Efe": [75, 80, 68],
}

GEÇME_NOTU = 60

def menu_goster():
    print(" Öğrenci Not Yönetim Sistemi ")
    print("a) Yeni bir öğrenci ekleme")
    print("b) Var olan bir öğrenciyi silme")
    print("c) Belirli bir öğrencinin not listesine yeni not ekleme")
    print("d) Bir öğrencinin notlarını görüntüleme")
    print("e) Bir öğrencinin not ortalamasını hesaplama")
    print("f) Bir öğrencinin geçme durumunu kontrol etme")
    print("g) Sınıfın genel ortalamasını hesaplama")
    print("h) Sınıftaki en yüksek ve en düşük notları bulma")
    print("i) Programdan çıkış")

def ogrenci_ekle():
    isim = input("Öğrencinin adını girin: ")
    if isim in ogrenciler:
        print("Bu öğrenci zaten mevcut!")
    else:
        ogrenciler[isim] = []
        print(f"{isim} sisteme eklendi.")

def ogrenci_sil():
    isim = input("Silmek istediğiniz öğrencinin adını girin: ")
    if isim in ogrenciler:
        del ogrenciler[isim]
        print(f"{isim} sistemden silindi.")
    else:
        print("Böyle bir öğrenci bulunamadı!")

def not_ekle():
    isim = input("Not eklemek istediğiniz öğrencinin adını girin: ")
    if isim in ogrenciler:
        try:
            not_ekle = int(input("Eklemek istediğiniz notu girin: "))
            ogrenciler[isim].append(not_ekle)
            print(f"{isim} için not başarıyla eklendi.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
    else:
        print("Böyle bir öğrenci bulunamadı!")

def notlari_goruntule():
    isim = input("Notlarını görmek istediğiniz öğrencinin adını girin: ")
    if isim in ogrenciler:
        print(f"{isim} öğrencisinin notları: {ogrenciler[isim]}")
    else:
        print("Böyle bir öğrenci bulunamadı!")

def ortalama_hesapla():
    isim = input("Not ortalamasını hesaplamak istediğiniz öğrencinin adını girin: ")
    if isim in ogrenciler:
        ortalama = sum(ogrenciler[isim]) / len(ogrenciler[isim])
        print(f"{isim} öğrencisinin not ortalaması: {ortalama:.2f}")
    else:
        print("Böyle bir öğrenci bulunamadı!")

def gecme_kontrol():
    isim = input("Geçme durumunu kontrol etmek istediğiniz öğrencinin adını girin: ")
    if isim in ogrenciler:
        ortalama = sum(ogrenciler[isim]) / len(ogrenciler[isim])
        durum = "Geçti" if ortalama >= GEÇME_NOTU else "Kaldı"
        print(f"{isim} öğrencisinin durumu: {durum}")
    else:
        print("Böyle bir öğrenci bulunamadı!")

def genel_ortalama():
    if ogrenciler:
        tum_notlar = [not_ for notlar in ogrenciler.values() for not_ in notlar]
        ortalama = sum(tum_notlar) / len(tum_notlar)
        print(f"Sınıfın genel not ortalaması: {ortalama:.2f}")
    else:
        print("Sistemde öğrenci bulunmamaktadır!")

def en_yuksek_en_dusuk():
    if ogrenciler:
        tum_notlar = [not_ for notlar in ogrenciler.values() for not_ in notlar]
        print(f"Sınıftaki en yüksek not: {max(tum_notlar)}")
        print(f"Sınıftaki en düşük not: {min(tum_notlar)}")
    else:
        print("Sistemde öğrenci bulunmamaktadır!")

while True:
    menu_goster()
    secim = input("Seçiminizi yapın (a-i): ").lower()

    if secim == "a":
        ogrenci_ekle()
    elif secim == "b":
        ogrenci_sil()
    elif secim == "c":
        not_ekle()
    elif secim == "d":
        notlari_goruntule()
    elif secim == "e":
        ortalama_hesapla()
    elif secim == "f":
        gecme_kontrol()
    elif secim == "g":
        genel_ortalama()
    elif secim == "h":
        en_yuksek_en_dusuk()
    elif secim == "i":
        print("Programdan çıkılıyor---")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin!")

