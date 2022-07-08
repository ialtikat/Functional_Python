# Functional_Python
Python ile fonksiyonel programlamayı anlattığım bir eğitim içeriğidir. 

Fonksiyonel Programlama
Bir bilgisayar programı dışarıdan bazı girdileri alır, onlar üzerinde işlem yapar ve bazı çıktılar üretir. Matematiksel bir gözle bakarsanız aslında bütün bir programın matematikteki bir fonksiyona benzediğini görürsünüz.
program(girdiler) = çıktılar
Fonksiyonel programlama, yalnızca fonksiyonların kullanılmasıyla yazılmış programlardır.

Fonksiyonel programların tipik özellikleri:
 Atama deyimi bulunmaz. Değişkenlerin değeri bir kere verildi mi, bir daha değişmez.
 Yan etkiler yoktur. Bir fonksiyonu çağırmak kendi sonucunu hesaplamaktan başka bir etki üretmez.

Python Programlama Dili
	Pythonda değişken tipi tanımlamaya gerek yoktur.  Değişkenlerimizin türünü type(değişken_adı) şeklinde yazarak kullandığımız değişkenin türünü görebiliriz.
a=45
print(type(a))

a="İbrahim ALTIKAT"
print(type(a))

a=4.5
print(type(a))

<class 'int'>
<class 'str'>
<class 'float'>

String (metin) ifade ile ilgili hangi fonksiyonları kullanabiliriz? Komutumuz dir(değişken_adi)
 Burada yer alan fonksiyonlar aynı zamanda gömülü fonksiyon olarak isimlendirilir. Yani bunları kullanmak için ekstra bir kütüphane yüklenmesine gerek yoktur.
a="Python İle Fonksiyonel Programlama"
print(dir(a))

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
 '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


Hangi fonksiyonları kullanacağımızı dir metotu ile gördük, peki nasıl kullanacağız. Komutumuzun adı help. Kullanılışı help(değişken_adi.gömülü_fonksiyon_ismi). Bu örnekte swapcase gömülü fonksiyonunun ne işe yaradığını varsa diğer giriş ve çıkış değerleri ile açıklamaları görüyoruz.
a="String ifade"
print(help(a.swapcase))

#Output
#Help on built-in function swapcase:

#swapcase() method of builtins.str instance
#    Convert uppercase characters to lowercase and lowercase characters to uppercase.

Sırada .format fonksiyonunu göstereceğim. Bu kullanımda tüm metin ifadelerini çift tırnak içinde yazarken, araya yerleşecek her değişken için {} (küme parantezleri) kullanıyoruz ve çift tırnaktan sonra .format(var1, var2 …) şeklinde sırası ile yazıyoruz.
a = 2
b = a**2
print("{}'nın karesi = {}".format(a,b))

# Output
# 2'nın karesi = 4

Bir diğer kullanım şekli kesirli sayıların yazdırılması. Bu örnekte virgülden sonra sadece 2 hane yazılmasını sağladık.
a = 2/3
print("a = ",a)
print("a ={:.2f}".format(a))

# Output
# a =  0.6666666666666666
# a =0.67
Format için bir başka örnek: parantezler içinde yazılacak rakamları format içinde yazılan değerlerin indisi olarak değerlendirilir.
print("{1} - {2} - {0}".format(3,1,2))

# Output
# 1 - 2 - 3

Tek satırlık açıklamalar için “#”
Çok satırlı açıklamalar için çok satırlı metini 3 er adet çift tırnak işareti içine alıyoruz.
#tek satırda açıklama için '#' işaretini kullanmalıyız.

"""  
   Çoklu satır kullanacağımız zaman
   yapmamamız gereken 3 tırnak içine 
   açıklama metnini yazmak. 
"""

Operatörler;
+ 	Toplama
- 	Çıkarma
*	Çarpma
** 	Üst alma
/ 	Bölme
// 	Tam sayı bölme
% 	Bölmeden kalan
+= 	Topla ve eşitle
-= 	Çıkar ve eşitle
*= 	Çarp ve eşitle
/= 	Böl ve eşitle
a = 9
b = a // 4
c = a % 4
d = a + b
e = a - b
f = a * b
g = a / b

print(
      "a =", a
      ,"b =", b
      ,"c =", c
      ,"d =", d
      ,"e =", e
      ,"f =", f
      ,"g =", g
)

# Output
# a = 9 b = 2 c = 1 d = 11 e = 7 f = 18 g = 4.5

a += b
b -= c
d *= e
e /= c

print(
       "a =", a
      ,"b =", b
      ,"d =", d
      ,"e =", e
)

# Output
# a = 11 b = 1 d = 77 e = 7.0

Karşılaştırma Operatörleri
•	==  	Eşit ise
•	!= 	Eşit değil ise
•	> 	Büyük ise
•	< 	Küçük ise
•	>= 	Büyük veya eşit ise
•	<= 	Küçük veya eşit ise
•	and
•	or
•	not
•	in
a = 18
b = 15
c = 15

if a < b:
      print("A Küçüktür B")
elif a > b:
      print("A Büyüktür B")
else:
      print("A Eşittir B")
      
# Output
# A Büyüktür B

if a > b and b == c:
      print("A Büyük B, B Eşittir C")

# Output
# A Büyük B, B Eşittir C

if a < b or b == c:
      print("B Eşittir C")
      
# Output
# B Eşittir C

Python sözdizimi gereği her satıra bir kod/komut gelmelidir. Ancak bazı kısaltma ifadeleri girintileme gibi kuralları bozmadan kısa kodlar yazmamızı sağlar. Aşağıdaki örnek else kısmı olmayan bir kısa if örneğidir.
a = 115
b = 100
if a > b: print("A Büyüktür B")

#   Output
#   A Büyüktür B

print("A Büyüktür B") if a > b else print("B Büyüktür A")

#   Output
#   A Büyüktür B

a = 30
b = 40
print("A Büyüktür B") if a > b else print("B Büyüktür A")

#   Output
#   B Büyüktür A

Listeler
a=[1,2,"a",3,5] 		# Dizilere benzerler ancak boyutları dinamiktir, ve karışık türden veriler içerebilirler.
x=list() 			# Boş liste oluşturur.
x=[] 			# Boş liste oluşturur.
len(a) 			# Eleman sayısı.
a.sort() 			# listeyi sıralar.
a.reverse() 		# listeyi ters çevirir.
a.pop() 			# son elemanı siler.
a.append("a") 		# sonuna yeni eleman ekler.
a.insert(indis, "a") 	# yeni elemanı belirtilen indise ekler. 
a.count(1)		# Bu eleman listede kaç tane var.
a.index(1) 		# Bu eleman kaçıncı indiste.
print a[1] 		# 1.indiste ki elemanı yazdır.
a[1]=2 			# 1.indisteki elemanın değerini değiştir.
del a[2] 		# 2.indisteki elemanı listeden sil.
>>> x = [1, 2, 3, 4]
>>> len(x)
4
>>> x.append(5)

>>> x
[1, 2, 3, 4, 5]
>>> x.pop()
5
>>> x
[1, 2, 3, 4]
>>> x.insert(0, -1)
>>> x
[-1, 1, 2, 3, 4]
>>> del x[0]
>>> x
[1, 2, 3, 4]
>>> x[1]
2
>>> x[-1]
4
>>> x[1:2]
[2]
>>> x[1:3]
[2, 3]
>>> x[1:-1]
[2, 3]
>>> x[0:-3]
[1]
>>> x.index(3)
2
>>> x.append(3)
>>> x
[1, 2, 3, 4, 3]
>>> x.count(3)
2
>>> 



