import unittest

class First(unittest.TestCase):
    def test_upper(self):
         #arrange
        test_string = "rubriks code"
        #act
        output = test_string.upper()
        #assert
        self.assertEqual(output, "RUBRIKS CODE")

if __name__ == '__main__':
    unittest.main()
