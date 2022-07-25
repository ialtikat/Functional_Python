"""
    Bir lambda işlevi, küçük bir anonim işlevdir.
    Bir lambda işlevi herhangi bir sayıda argüman alabilir, ancak yalnızca bir ifadeye sahip olabilir.
    Python dilinde fonksiyonları n def anahtar sözcüğü ile oluşturulduğu biliyoruz. Bu fonksiyonlar tanımlanır,
      çağrılır ve return ile geriye bir değer/nesne döndürerek çalışırlar.
"""

def carp(a, b):
  return a * b

carp_1 = lambda a, b : a * b

# Lambda ise küçük ve anonim fonksiyonlar oluşturmamızı sağlar.
print(carp(3, 5))
print(carp_1(3, 5))
# Output
# 15
# 15


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
# Output
# 13

"""
    lambda argümanları: ifade
    syntax yapısı yukarıda gösterildiği gibidir.
"""