import math
import unittest

def sin(x):
    return sin_wrapped(x, 107, True, 0)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1) 

def sin_wrapped(x, depth, sign, sum):
    if depth == 1:
        return x + sum
    else:
        if sign == True:
            return sin_wrapped(x, depth-2, False, sum-(x**depth/factorial(depth)))
        else:
            return sin_wrapped(x, depth-2, True, sum+(x**depth/factorial(depth)))

class TestStringMethods(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_sin(self):
        print("sin(0) = ", sin(0))
        print("sin(PI/4) = ", sin(math.pi/4))
        print("sin(PI/2) = ", sin(math.pi/2))
        print("sin(3PI/4) = ", sin((3*math.pi)/2))
        print("sin(PI) = ", sin(math.pi))

if __name__ == '__main__':
    unittest.main()
