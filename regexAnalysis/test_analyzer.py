import unittest
from analyzer import Analyzer


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.testFile = Analyzer('class Rectangle this.height this.width \
                                   function area() function calcArea()\
                                  this.height this.Width')

    def test_find_class(self):
        self.assertEqual(self.testFile.find_class, 'Rectangle')

    def test_find_property(self):
        self.assertEqual(self.testFile.find_property, 'height\l width\l')

    def test_find_function_1(self):
        self.assertEqual(self.testFile.find_function_1,
                         'get()\l calcArea()\l')

if __name__ == '__main__':
    unittest.main()
