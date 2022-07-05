"""
      Karşılaştırma Operatörleri
      
	==  	Eşit ise
	!= 	Eşit değil ise
	> 	Büyük ise
	< 	Küçük ise
	>= 	Büyük veya eşit ise
	<= 	Küçük veya eşit ise
	and
	or
	not
	in

"""

a = 18
b = 15
c = 15

if a < b:
      print("A Küçüktür B")
elif a > b:
      print("A Büyüktür B")
else:
      print("A Eşittir B")
      
# Output
# A Büyüktür B

if a > b and b == c:
      print("A Büyük B, B Eşittir C")

# Output
# A Büyük B, B Eşittir C

if a < b or b == c:
      print("B Eşittir C")
      
# Output
# B Eşittir C