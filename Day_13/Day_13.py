"""
    Her string bir karakter dizisidir ve mutable nesnelerdir. Dolayısı ile
    doğrudan itere edilebilirler. İndislerin 0 dan başladığını unutmayalım.
"""
x = "Python programlama"

for i in x:
    print(i)
# Output
# P
# y
# t
# h
# o
# n

# p
# r
# o
# g
# r
# a
# m
# l
# a
# m
# a    

print(x[4])
# Output
# o

"""
    Stringleri bölmek. Stringlerden (Listeler içinde aynı şey geçerlidir) ile belirli aralıkları parçalayabiliriz.
"""

a = "Python ile fonksiyonel programlama"

print(a[2:10])  # 2'den 10.indise kadar.
# Output
# thon ile

print(a[2:])    # 2'den sonuna kadar.
# Output
# thon ile fonksiyonel programlama

print(a[:10])   # Baştan 10.indise kadar.
# Output
# Python ile

print(a[0::2])  # Baştan sona ikişer adımla.
# Output
# Pto l okioe rgalm

print(a[::-1])  # Sondan başa -1 adıma, tersten yazdırmak.
# Output
# amalmargorp lenoyisknof eli nohtyP

b = "Python programlama, dili"

print(b.strip(' '))
# Output
# Python programlama, dili

print(b.replace(',', ' '))
# Output
# Python programlama  dili

print(b.upper())
# Output
# PYTHON PROGRAMLAMA, DILI

print(b.lower())
# Output
# python programlama, dili

print(b.split(' '))
# Output
# ['Python', 'programlama,', 'dili']