"""
    Zip 
    İki farklı listeyi birleştirmek için kullanılır.
    Bir fermuar gibi düşünebiliriz.
"""
from doctest import OutputChecker


x = [1, 2, 3, 4, 5]
y = ["Bir", "İki", "Üç", "Dört", "Beş"]
z = list(zip(x, y))
print(z)
# Output
# [(1, 'Bir'), (2, 'İki'), (3, 'Üç'), (4, 'Dört'), (5, 'Beş')]

# Zip işlemini kullanarak sözlük yapısını elde edelim.
x = [1, 2, 3, 4, 5]
y = ["Bir", "İki", "Üç", "Dört", "Beş"]
z = dict(zip(y, x))
print(z)
# Output
# {'Bir': 1, 'İki': 2, 'Üç': 3, 'Dört': 4, 'Beş': 5}