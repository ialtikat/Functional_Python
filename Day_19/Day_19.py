"""
    Map 
    Itere edilebilir nesneleri parametre olarak alır ve her öğe için işletir.
"""

#Pratik olarak şöyle düşünebiliriz. Map itere edilebilir bir nesnedeki her öğeyi sırasıyla,işler.
def f(a): return a * a
x = map(f, [1, 2, 3, 4])
print(list(x))
# Output
# [1, 4, 9, 16]

# List olarak çevirme işlemi yapmadığımız zaman hata alıyoruz.
print(x)
# Output
# <map object at 0x000002C9AFE90850>

# Lambda ile birlikte kullanalım.
f = lambda a: a * a
x = map(f, [1, 2, 3, 4])
print(list(x))
# Output
# [1, 4, 9, 16]

# Aşağıda gördüğümüz gibi yukarıda yer alan örneğinin aynısıdır. Aralarındaki fark satır sayısıdır.
print(list(map(lambda a: a * a, [1, 2, 3, 4])))
# Output
# [1, 4, 9, 16]

# Map ile string listeleri karşışıklı birleştirme örneği.
f = lambda a, b : a + " " + b
x = map(f, ["python", "dili", "fonksiyonel"],
        ["programlama", "ile", "programlama"])
print(list(x))
# Output
# ['python programlama', 'dili ile', 'fonksiyonel programlama']