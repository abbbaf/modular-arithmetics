from modular_arithmetics import Modulus, gcd
from random import randint

#NIST Curve P-192
p = Modulus(2**192-2**64-1) 
n = 6277101735386680763835789423176059013767194773182842284081
a = -3 % p 

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def __mul__(self,k):
        k = int(k)
        q = Point(self.x,self.y)
        for b in bin(k)[3:]:
            lamda = (3*q.x**2 + a)/(2*q.y)
            x = lamda**2 - 2*q.x
            y = lamda*(q.x - x) - q.y
            q.x, q.y = x, y
            if (b == '1'):
                lamda = (q.y - self.y)/(q.x - self.x)
                x = lamda**2 - self.x - q.x
                y = lamda*(self.x - x) - self.y 
                q.x, q.y = x, y
        return Point(q.x, q.y)


    def __rmul__(self,k):
        return self.__mul__(k)

    
    def __imul__(self,k):
        result = self.__mul__(k)
        self.x = result.x
        self.y = result.y
        return self

    
    def __eq__(self,p):
        return self.x == p.x and self.y == p.y


    def __repr__(self):
        return str(self.x) + ", " + str(self.y)


G = Point(602046282375688656758213480587526111916698976636884684818 % p,174050332293622031404857552280219410364023488927386650641 % p)



class ECC():
    
    def __init__(self):
        self.d = randint(2,n-1)
        self.__publicKey = self.d*G

    
    @property
    def publicKey(self):
        return self.__publicKey


    def createSharedKey(self,publicKey):
        return self.d*publicKey


    
