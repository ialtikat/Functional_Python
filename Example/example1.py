"""
    Python ile yapmış olduğum kısa bir örnek.
"""


Ogrenciler=[]
OgrenciNot=[]
Ortalama = 0

def NotHesap ():
    print("NOT GİRİŞİ")
    for i in range(len(Ogrenciler)):
        print("--------------------------------------------------------")
        print(Ogrenciler[i])
        while True:
            try:
                Not_1 = int(input("1.Sınav Notunu Giriniz :"))
                Not_2 = int(input("2.Sınav Notunu Giriniz :"))
                if Not_1 >=0 and Not_1 <=100 and Not_2 >= 0  and Not_2 <= 100:
                    break
                else:
                    print("Lütfen sınav notlarını 0-100 değerleri arasında giriniz!")
            except:
                print("Lütfen geçerli bir sayı giriniz!")
        Ortalama = (Not_1 + Not_2)/2
        OgrenciNot.append(Ortalama)

def OgrenciAd():
    while True:
        try:
            OgrenciSayisi= int(input("Öğrenci Sayısını Giriniz :"))
            print("--------------------------------------------------------")
            for i in range(OgrenciSayisi):
                OgrenciAdı=input("Öğrenci Adını Giriniz :")
                Ogrenciler.append(OgrenciAdı)
            print("********************************************************")        
            break
        except:
            print("Lütfen geçerli bir sayı giriniz!")
        
        
if __name__== "__main__":
    OgrenciAd()
    NotHesap()
    print("********************************************************")
    print("DERS ORTALAMALARI")
    for i in range(len(Ogrenciler)):
        print(Ogrenciler[i] ," : ", OgrenciNot[i])
    
