from modular_arithmetics import Modulus, gcd
from primarity_test import generateRandomPrime



class RSA:


    def __init__(self,*args):
        if len(args) > 2:
            raise TypeError('Number of arguments can either be 1 or 2')
        if len(args) == 1:
            self.e = 65537
            bits = args[0]
            lamda = None
            while True:
                p = generateRandomPrime(bits >> 1)
                q = generateRandomPrime(bits >> 1)
                self.n = Modulus(p*q)
                lamda = (p-1)*(q-1)//gcd(p-1,q-1)
                self.e %= Modulus(lamda)
                if gcd(self.e,lamda) == 1: 
                    break 
            
            self.d = self.e**-1
            
            self.e %= self.n
            self.d %= self.n
        else:
            self.n = Modulus(args[0])
            self.e = args[1] % n

        
    def getParameters(self):
        return int(self.n), int(self.e)


    def encrypt(self,m):
        return m**self.e
    
    
    def decrypt(self,c):
        return c**self.d
    

