import euler as e
import unittest

class IntegrateTest(unittest.TestCase):
    '''
        Test the Integrate Method from Euler PYX, using the simplest case.
    '''
    def test(self):
        self.assertEqual(1, e.integrate(1, 0, h=1))
        self.assertEqual(2, e.integrate(1, 1, h=1))
        self.assertEqual(4, e.integrate(1, 2, h=1))
        self.assertEqual(8, e.integrate(1, 3, h=1))
        self.assertEqual(16, e.integrate(1, 4, h=1))

if __name__ == '__main__':
    unittest.main()