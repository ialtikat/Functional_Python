x = [1, 2, 3, 4, 5, 6, 7]

for i in x:
    print(i)
    
# Output
# 1
# 2
# 3
# 4
# 5
# 6
# 7

"""
    For ile liste içerisinde yer alan sayıları toplamını bulalım.
    For ile sayıların toplamını bulduk lakin bunu hazır fonksiyon olan sum() fonksiyonu ile de yapabiliriz.
    İki örneğin kullanımını aşağıdaki örnekte bulabilirsiniz.

"""
t = 0
for i in x:
    t+=i
print("Toplam = ",t)
print("Sum ile bulunan toplam = ", sum(x))

# Output
# Toplam =  28
# Sum ile bulunan toplam =  28


"""
    -Range komutunun kullanımını göreceğiz.
    -Gerek döngülerde gerekse bir değer aralığı oluşturmak istenildiğinde kullanılır.  
    -Range 1-3 arası parametre alır. 2 ve 3. değerler tercihe göre kullanılır.
    Örnek kullanımları;
        - range(5)          => 0, 1, 2, 3, 4
        - range(2, 5)       => 2,3,4
        - range(1, 10, 2)   => 1, 3, 5, 7, 9
    * Dikkat edelim son sayılar aralığa dahil edilmez. Aralıklar varsayılan olarak küçükten büyüğe kurgulanır.
        - range(10, 5, -1)  => 10, 9, 8, 7, 6
"""
x = range(10, 5, -1)
for i in x:
    print(i)

# Output
# 10
# 9
# 8
# 7
# 6

for i in range(10, 5, -1):
    print(i)
    
# Output
# 10
# 9
# 8
# 7
# 6
