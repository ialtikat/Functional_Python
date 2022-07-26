"""
    Ortalamadan %20 daha uzak olanları seçen bir liste üreteci.
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yuzde = 20

y = [i for i in x if ( i > ((yuzde + 100) * sum(x)) / (len(x) * 100) or 
                        i < ((100 - yuzde) * sum(x)) / (len(x) * 100) )]
print(y)

#   Output
#   [0, 1, 2, 3, 7, 8, 9, 10]

"""
    sum() liste içerisinde yer alan değerlerin toplamını veren hazır fonksiyon.
    len() listenin uzunluğunu veren hazır fonksiyon. (liste içerisinde yer alan elaman sayısı.)
    or = if-else yapısında veya olarak kullanılır.
    and = if-else yapısında ve olarak kullanılır.
    ikisi arasında ki fark or'da verilen iki şarttan birinin sağlanması yeterli
    and'de ise verilen iki şarttında sağlanma zorunluluğu vardır.
    
    or için => 1 or 0 = 1
               0 or 1 = 1
               1 or 1 = 1
               0 or 0 = 0
    and için =>1 and 0 = 0
               0 and 1 = 0
               1 and 1 = 1
               0 and 0 = 0
"""


# Kullanıcı adlarında istenmeyen karakter olan kullanıcıları listeleme.
sifreler = ["ali123.", "veli!12", "kalem", "kelam", "kamil", "gel.123"]
a = [i for i in sifreler if "." in i]
print(a)
# Output
# ['ali123.', 'gel.123']

