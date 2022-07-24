"""
    Listeler gibi kullanılırlar ama güncellenemezler.
"""
>>> x = ()
>>> type(x)
<class 'tuple'>
>>> x = ("Mehmet","Akif","Ersoy",1)
>>> x
('Mehmet', 'Akif', 'Ersoy', 1)
>>> x[0]
'Mehmet'
>>> x[0]="İstiklal"
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x[0]="İstiklal"
TypeError: 'tuple' object does not support item assignment
>>> x.append("istiklal")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x.append("istiklal")
AttributeError: 'tuple' object has no attribute 'append'
>>> len(x)
4
>>> x
('Mehmet', 'Akif', 'Ersoy', 1)
>>> x.count("mehmet")
0
>>> x.count("Mehmet")
1
>>> x.index("Akif")
1
"""
    Tuple güncelleme işlemi yapmak için önce listeye çevirip ardından tekrar tuple'a çevirmek gerekmektedir.    
"""
>>> y = list(x)
>>> y[1] = "İstiklal"
>>> x = tuple(y)
>>> x
('Mehmet', 'İstiklal', 'Ersoy', 1)

#   Çoklu atama işlemi.

>>> bilgiler = ("Ahmet", "1234")
>>> user, password = bilgiler
>>> user
'Ahmet'
>>> password
'1234'