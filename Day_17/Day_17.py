"""
    Dictionary (sözlük) yapısının kullanımı. Sölükler Key ve value şeklinde bir yapıya sahiptir.
"""
from re import A


x = {"User" : "İbrahim", "Şifre" : "1234", "Şehir" : "Samsun"}

# Erişim 
print(x['User'])
# Output
# İbrahim

# Güncelleme
x["User"] = "İbrahim ALTIKAT"
print(x)
# Output
# {'User': 'İbrahim ALTIKAT', 'Şifre': '1234', 'Şehir': 'Samsun'}


# Yeni key-value ekleme
x['TC Kimlik'] = "12345678910"
print(x)
# Output
# {'User': 'İbrahim ALTIKAT', 'Şifre': '1234', 'Şehir': 'Samsun', 'TC Kimlik': '12345678910'}

# Key-Value silme
x.pop("TC Kimlik")
print(x)
# Output
# {'User': 'İbrahim ALTIKAT', 'Şifre': '1234', 'Şehir': 'Samsun'}


# Dict eleman sayısı
print(len(x))
# Output
# 3

# Doğrudan itere edilebilirler.
for k,v in x.items():
  print(k, ":", v)
# Output
# User : İbrahim ALTIKAT
# Şifre : 1234
# Şehir : Samsun  

for k in x.keys():
  print(k)
# Output
# User
# Şifre
# Şehir

for v in x.values():
  print(v)
# Output
# İbrahim ALTIKAT
# 1234
# Samsun

# Alternatif erişim yapıları oluşturulabilir.
u, p, lc = x.values()
print(u, p, lc)
# Output
# İbrahim ALTIKAT 1234 Samsun

a = list(x.values())
print(a[0])
# Output
# İbrahim ALTIKAT

"""
  Liste oluşturmak için list() fonksiyonunu
  Sözlük yapısı oluşturmak için dict() yapısını kullanabiliriz.  
"""

a = list(range(1,5))
b = [i for i in a]
print(b)
# Output
# [1, 2, 3, 4]

c = [i**2 for i in a]
print(c)
# Output
# [1, 4, 9, 16]

# İç içe sözlük oluşturma.
d = [{str(i) : i} for i in a]
print(d)
# Output
# [{'1': 1}, {'2': 2}, {'3': 3}, {'4': 4}]

#Listeden sayısal olmayanları eleyelim.
x = ["a",1, 2, 3, "b", "c", 4, 5, 6]
y = [i for i in x if str(i).isdigit()]
print(y)
# Output
# [1, 2, 3, 4, 5, 6]
"""
    isdigit = verilen değerde rakam olup olmadığını kontrol eder.
"""
# Verilen değer tamamen rakamlardan oluştuğu için dönüş true dur.
>>> '123'.isdigit()
True
# Verilen değerde harfler olduğu için çıktı false olarak dönmüştür. 
>>> '123abc'.isdigit()
False
# Verilen değerde rakamlardan oluşmasına rağmen başında boşluk olduğu için geri dönüş olarak false değerini döndürmüştür.
>>> ' 123'.isdigit()
False
# Verilen değer rakam harici bir değer içerdiği için çıktısı false'dur.
>>> '1.23'.isdigit()
False