"""
    Döngülerle birlikte;
        > Break: Döngüyü kırmak (bitirmek) için kullanılır. İç içe döngülerde ise sadece içerisinde bulunduğu döngüyü kırmaktadır.
        > Continue: Döngülerde oluşan şartın gerçekleşmemesi ve bir sonraki duruma geçmesi için kullanılır. Yani o işlemi pas geçmek için tercih edilir.
        
"""

for i in range(1, 10):
    if i % 2 == 0:
        continue
    elif i % 5 == 0:
        break
    else:
        print(i)
    
#  Çift sayılar pas geçilir ve 5’e geldiğinde döngü sonlandırılır.
# Output
# 1
# 3

"""
    Asal sayı örneği    
"""

asal = True
x = 17
for i in range(3, x):
    if x % i == 0:
        asal = False
        break

print(x, " asaldır.") if asal else print(x, " asal değildir.")

# Output
# 17  asaldır.

"""
    For-else kullanımı ile asal sayı örneği
"""
x = 18
for i in range(3, x):
    if x % i == 0:
        print(x, "asal değildir.")
        break
else:
    print(x, "asaldır.")
    
# Output
# 18 asal değildir.
# Burada else kullanımı gerekli bir kullanım değil.

