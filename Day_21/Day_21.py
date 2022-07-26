"""
    filter() filter(function, iterable) : filter fonksiyonu parametre olarak fonksiyon ve liste, 
    demet gibi döngüye sokulabilecek veri alır. 
    Geriye true koşulunu sağlayan değerleri döndürür.
"""
kisiler = ['Mehmet', 'Akif', 'ERSOY']
tarihler = [1920, 1919, 1921]
print(list(filter(lambda zipped : 1920 <= zipped[1] <= 1921, zip(kisiler, tarihler))))
#  Output
#  [('Mehmet', 1920), ('ERSOY', 1921)]


print(list(filter(lambda a : a % 2 == 0, list(range(10)))))
# Output
# [0, 2, 4, 6, 8]


liste = [2, 8, 4, 1, 6, 3, 7, 8 ,9]
besden_buyuk = list( filter( lambda x : x >5 , liste))
print( besden_buyuk ) 
# Output
# [8, 6, 7, 8, 9]