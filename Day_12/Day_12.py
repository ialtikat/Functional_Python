"""
    Random kütüphanesi, rast gele sayılar üretmek için kullandığımız bir fonksiyondur. 
    Kütüphaneleri çalışma dosyamıza eklemek için "import" komutunu kullanıyoruz.
"""
import random

print(random.random())
# Output
# 0.11203194141555595

print((int)((10)*random.random()))
# Output
# 4

"""
    - Shuffle , choice, sample
    - Choice listeden tek bir elemanı rastgele seçer.
    - Sample ise parametre sayısı olarak verilen kadar rastgele eleman seçer.
    - Shuffle elemanları karıştırır.
"""
x = [1, 2, 3, 'a', 'b']

print(random.choice(x))
# Output
# a

print(random.sample(x, 2))
# Output
# ['b', 2]

random.shuffle(x)
print(x)
# Output
# ['b', 3, 1, 'a', 2]