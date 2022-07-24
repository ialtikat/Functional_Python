"""
    Kümeler, indeksleri yoktur, çift değer içermezler.
"""

>>> x = {1,1,2,3,2,1,5,6,5,8,1,2,3,4,5,6,7,8,9,10}
>>> x
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> len(x)
10
>>> x[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x[0]
TypeError: 'set' object is not subscriptable
>>> 1 in x
True
>>> x.update({11,12,13,15})
>>> x
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15}