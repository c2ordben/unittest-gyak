import unittest

def fibo(n :int):
    tmp = 1
    tmpketto = 0
    tmpharom = 0
    if n <= 0:
        return 0
    for i in range(0,n-1):
        tmpharom = tmpketto
        tmpketto = tmp
        tmp = tmpketto + tmpharom
    return tmp
    
class Testfibo(unittest.TestCase):
    def Neg(self):
        self.assertEqual(fibo(-2),0)
    def nulla(self):
        self.assertEqual(fibo(0),0)
    def elsopoz(self):
        self.assertEqual(fibo(5),3)
    def masodikpoz(self):
        self.assertEqual(fibo(11),55)
    def harmadikpoz(self):
        self.assertEqual(fibo(7),8)

if __name__ == "__main__":
    unittest.main()
