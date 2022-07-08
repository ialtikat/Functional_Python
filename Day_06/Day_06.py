"""
    a=[1,2,"a",3,5] 		# Dizilere benzerler ancak boyutları dinamiktir, ve karışık türden veriler içerebilirler.
    x=list() 			    # Boş liste oluşturur.
    x=[] 			        # Boş liste oluşturur.
    len(a) 			        # Eleman sayısı.
    a.sort() 			    # listeyi sıralar.
    a.reverse() 		    # listeyi ters çevirir.
    a.pop() 			    # son elemanı siler.
    a.append("a") 		    # sonuna yeni eleman ekler.
    a.insert(indis, "a") 	# yeni elemanı belirtilen indise ekler. 
    a.count(1)		        # Bu eleman listede kaç tane var.
    a.index(1) 		        # Bu eleman kaçıncı indiste.
    print a[1] 		        # 1.indiste ki elemanı yazdır.
    a[1]=2 			        # 1.indisteki elemanın değerini değiştir.
    del a[2] 		        # 2.indisteki elemanı listeden sil.

"""
>>> x = [1, 2, 3, 4]
>>> len(x)
4
>>> x.append(5)

>>> x
[1, 2, 3, 4, 5]
>>> x.pop()
5
>>> x
[1, 2, 3, 4]
>>> x.insert(0, -1)
>>> x
[-1, 1, 2, 3, 4]
>>> del x[0]
>>> x
[1, 2, 3, 4]
>>> x[1]
2
>>> x[-1]
4
>>> x[1:2]
[2]
>>> x[1:3]
[2, 3]
>>> x[1:-1]
[2, 3]
>>> x[0:-3]
[1]
>>> x.index(3)
2
>>> x.append(3)
>>> x
[1, 2, 3, 4, 3]
>>> x.count(3)
2
>>> 