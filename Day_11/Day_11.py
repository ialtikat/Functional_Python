"""
    class anahtar sözcüğü ile oluşturulur, sınıf ismini verirken büyük harf zorunludur.
    __init__ metotu yapılandırıcı metottur.
    Self anahtar sözcüğü kullanımı zorunludur.
"""
class Matematik:
    
    def __init__(self):
        self.pi = 3.14
    
    
    def alan_hesaplama(self, r = 0):
        return self.pi * (r**2)
    
    def cevre_hesaplama(self, r = 0):
        return self.pi * 2 * r


daire = Matematik()

print("Daire alan hesabı : ",daire.alan_hesaplama(4))
print("Daire çevre hesabı : ",daire.cevre_hesaplama(4))

"""
    Output:
    Daire alan hesabı :  50.24
    Daire çevre hesabı :  25.12
"""
