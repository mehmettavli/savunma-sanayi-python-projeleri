print("=" * 50)
print(" OTONOM DRONE GÖREV SİSTEMİ")
print("=" * 50)

# BÖLÜM 1: KALKIŞ
print("\n AŞAMA 1: KALKIŞ")
print("-" * 50)

yukseklik = 0
hedef_yukseklik = 50
batarya = 100

for yukseklik in range(0, hedef_yukseklik + 1, 10):
    print(f" Yükseklik: {yukseklik}m |  Batarya: %{batarya}")
    batarya -= 2

print(" Hedef yüksekliğe ulaşıldı!")

# BÖLÜM 2: GÖREV UÇUŞU
print("\n AŞAMA 2: GÖREV UÇUŞU")
print("-" * 50)

gorev_suresi = 0
maksimum_sure = 10
yonler = ["Kuzey","Doğu","Doğu","Kuzey","Batı","Batı","Güney","Güney","Doğu","Doğu"]

while gorev_suresi < maksimum_sure and batarya > 50:
    for yon in yonler:
        # Döngü içinde de kontrol et
        if gorev_suresi >= maksimum_sure or batarya <= 50:
            break
        
        print(f" {yon} yönünde hareket ediyor.")
        gorev_suresi += 1
        batarya -= 3
        print(f" Süre: {gorev_suresi}s |  Batarya: %{batarya} |  Görüntü alınıyor...")

# DURUM KONTROLÜ
if batarya <= 50:
    print("\n Batarya düşük! Görev sonlandırılıyor.")
    print(" ACİL İNİŞ BAŞLADI!")
    print("-" * 50)
    
    while yukseklik > 0:
        batarya -= 1
        yukseklik -= 20
        if yukseklik < 0:
            yukseklik = 0  # Negatif olmasın
        print(f" Yükseklik: {yukseklik}m |  Batarya: %{batarya}")
    
    print(" Acil iniş tamamlandı!")
    
else:
    print("\n Görev tamamlandı!")
    
    # BÖLÜM 3: NORMAL İNİŞ
    print("\n AŞAMA 3: NORMAL İNİŞ")
    print("-" * 50)
    
    while yukseklik > 0:
        print(f" Yükseklik: {yukseklik}m |  Batarya: %{batarya}")
        yukseklik -= 10
        batarya -= 1
    
    print(" İniş tamamlandı!")

# SONUÇ
print(f"\n GÖREV RAPORU")
print("=" * 50)
print(f" Kalan batarya: %{batarya}")
print(f" Son yükseklik: {yukseklik}m")
print(f" Toplam görev süresi: {gorev_suresi}s")
print("=" * 50)