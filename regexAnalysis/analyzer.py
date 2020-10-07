import re
#from interface import Interface

class Analyzer:
    def __init__(self):
        self.js_file = " class Rectangle constructor (height, width) {this.height = height;\
            this.width = width;} get class area(){return this.calcArea();}  \
            this.speed = speed;        this.name = name;\
            calcArea() { function return this.height * this.width; }}const square = \
            function new Rectangle (10, 10);console.log(square.area);"

    def find_class(self):
        #  class_name_finder = re.match(r'^class.(\w+)', self.js_file)
        #Use search instead of match as match only searches the first line.
        global class_name
        class_name = re.search(r'class.(\w+)', self.js_file)
        if class_name is not None:
            class_name = class_name.group().split()[-1]
            print(class_name)
            """global classList
            classList = [class_name]
            print(classList)"""

    def find_property(self):
        global property_name
        property_name = re.findall(r'this.(\w+)', self.js_file)
        if property_name is not None:
            first_list = property_name
            print(first_list)
            property_name = list(dict.fromkeys(first_list))
            property_name = (['{}\l'.format(i) for  i in property_name])
            property_name = " ".join(property_name)
            print(property_name)

    def find_function_1(self):
        global function_name
        function_name = re.findall(r'function.(\w+)', self.js_file)
        if function_name is not None:
            function_name = function_name
            function_name = (['{}()\l'.format(i) for i in function_name])
            function_name = " ".join((function_name))
            print(function_name)

    def create_file(self):
        dot_file1 = open("classfile.dot", "w")
        dot_file1.write(f'digraph G {{fontname = "Bitstream Vera Sans"\
fontsize = 8 node [fontname = "Bitstream Vera Sans"\
fontsize = 8 shape = "record"]\
edge [fontname = "Bitstream Vera Sans"fontsize = 8]\
 {class_name}[ label = " {{{class_name}| {property_name}|{function_name}}}"]}}')
        dot_file1.close()
        dot_file1 = open("classfile.dot", "r")
        print(dot_file1.read())
