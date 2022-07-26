"""
    reduce fonksiyonu parametre olarak fonksiyon ve liste, demet gibi döngüye sokulabilecek veri alır.
"""

from functools import reduce

sayilar = [1, 3, 5, 7, 9]
toplam = reduce (lambda x, y : x + y, sayilar )
print( toplam )
# Output
# 25

f = lambda a, b : a + b
s = reduce(f, [1, 2, 3, 4])
print(s)
# Output
# 10

# Faktöriyel hesabı. (1, 2, 3, 4)
print(reduce(lambda a1, a2 : a1 * a2, range(1,5)))
# Output
# 24
