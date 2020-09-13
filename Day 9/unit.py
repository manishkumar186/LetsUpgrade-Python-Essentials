import unittest
import question1
class prime(unittest.TestCase):
    def prime_number(self):
        k = 6
        result=question1.prime(k)
        self.assertEquals(result,"{} is a prime number".format(k))
if __name__ == '__main__':
    unittest.main()