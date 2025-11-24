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
    def test_Neg(self):
        self.assertEqual(fibo(-2),0)
    def test_nulla(self):
        self.assertEqual(fibo(0),0)
    def test_elsopoz(self):
        self.assertEqual(fibo(5),5)
    def test_masodikpoz(self):
        self.assertEqual(fibo(10),55)
    def test_harmadikpoz(self):
        self.assertEqual(fibo(7),12)

if __name__ == "__main__":
    unittest.main()

print(fibo(2))