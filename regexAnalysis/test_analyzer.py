import unittest
from analyzer import Analyzer


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.testFile = Analyzer('class Rectangle this.height this.width \
                                   function area() function calcArea()\
                                  this.height this.Width')

        self.testFile2 = Analyzer('class Rectangle this.height this.width \
                                   function area() function calcArea()\
                                  this.height this.width')

        self.testFile3 = Analyzer('class Rectangle this.Height this.width \
                                           function area() function calcArea()\
                                          this.height this.Width')
        self.testFile4 = Analyzer('')


        self.testFile6 = Analyzer('class Rectangle \
                                        function area() function calcArea()')


        self.testFile5 = Analyzer(' class Rectangle this.height this.width \
                                              this.height this.Width')
        self.testFile7 = Analyzer(' Rectangle this.height this.width \
                                           function area() function calcArea()\
                                          this.height this.Width')

        self.testFile8 = Analyzer('class Rectangle \
                                               function area function calcArea')


    def test_find_class(self):
        expected = 'Rectangle'
        self.testFile.find_class()
        actual = self.testFile.get_class_name()
        self.assertEqual(expected, actual)

    def test_find_class_name(self):
        expected = None
        self.testFile7.find_class()
        actual = self.testFile7.get_class_name()
        self.assertEqual(expected, actual)

    def test_no_js_file(self):
        expected = 'A JS file needs to be selected to run the analyzer'
        self.testFile4.find_class()
        actual = self.testFile4.get_no_file()
        self.assertEqual(expected, actual)

    def test_find_property(self):
        expected = 'height\l width\l'
        self.testFile.find_property()
        actual = self.testFile.get_property_name()
        self.assertEqual(expected, actual)

    def test_no_property(self):
        expected = ''
        self.testFile6.find_property()
        actual = self.testFile6.get_property_name()
        self.assertEqual(expected, actual)

    def test_double_ups(self):
        expected = 'height\l width\l'
        self.testFile2.find_property()
        actual = self.testFile2.get_property_name()
        self.assertEqual(expected, actual)

    def test_lower_case(self):
        expected = 'height\l width\l'
        self.testFile3.find_property()
        actual = self.testFile3.get_property_name()
        self.assertEqual(expected, actual)

    def test_find_function_1(self):
        expected = 'area()\l calcArea()\l'
        self.testFile.find_function_1()
        actual = self.testFile.get_function_name()
        self.assertEqual(expected, actual)

    def test_no_brackets_function_1(self):
        expected = 'area()\l calcArea()\l'
        self.testFile8.find_function_1()
        actual = self.testFile8.get_function_name()
        self.assertEqual(expected, actual)

    def test_no_function_1(self):
        expected = ''
        self.testFile5.find_function_1()
        actual = self.testFile5.get_function_name()
        self.assertEqual(expected, actual)

    # def test_dot_file1(self):
    #     expected = 'digraph G {fontname = "Bitstream Vera Sans"fontsize = 8 node [fontname = "Bitstream Vera Sans"fontsize = 8 shape = "record"]edge [fontname = "Bitstream Vera Sans"fontsize = 8] Rectangle[ label = " {Rectangle| height\l width\l|get()\l calcArea()\l}"]}'
    #     self.testFile2.create_file()
    #     actual = self.testFile2.do_get_create_file()
    #     self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
