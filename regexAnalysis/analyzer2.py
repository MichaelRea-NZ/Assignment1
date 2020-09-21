import re


class Analyzer:
    def __init__(self):
        self.js_file = " Rectangle class constructor (height, width) {this.height = height;\
            this.width = width;} get class area(){return this.calcArea();}  \
            this.speed = speed;        this.name = name;\
            calcArea() { function return this.height * this.width; }}const square = \
            function new Rectangle (10, 10);console.log(square.area);"

    def find_class(self):
        #  class_name_finder = re.match(r'^class.(\w+)', self.js_file)
        class_name_finder = re.search(r'class.(\w+)', self.js_file)
        if class_name_finder is not None:
            class_name = class_name_finder.group().split()[-1]
            print(class_name)
            global classList
            classList = [class_name]
            print(classList)
            # self.find_class(class_name_finder, self.js_file)

    # def find_class(func, js_file):
    #     print(js_file)
    #     class_name_finder = re.match(r'^class.(\w+)', js_file)
    #     if class_name_finder is not None:
    #         print(class_name_finder.group().split()[-1] + '\n')
    #         class_name = class_name_finder.group().split()[-1]
    #         print(class_name)
    #         find_class(class_name_finder, js_file)

    def find_property(self):
        property_declaration = re.findall(r'this.(\w+)', self.js_file)
        if property_declaration is not None:
            first_list = property_declaration
            print(first_list)
            global property_name
            property_name = list(dict.fromkeys(first_list))
            print(property_name)

    def find_function_1(self):
        func_declaration_1 = re.findall(r'function.(\w+)', self.js_file)
        if func_declaration_1 is not None:
            global function_name
            function_name = func_declaration_1
            print(function_name)

    def combined_declarations(self):
        global names
        names = [classList, property_name, function_name]
        print(names)

    # def find_function_2(self):
    # func_declaration_2 = re.findall(r'\w+ ?=[=\\.+)=>]', self.js_file)
    # if func_declaration_2 is not None:
    # function_name =func_declaration_2
    # print(function_name)


"""func_declaration_1 = re.findall(r'^function.(\w+)', js_file)
func_declaration_2 = re.findall(r' \w+ ?=[= (.+) =>]', js_file)
def find_function(func, js_file):
    if find_function is not None:
        function_list.append(func.group().split()[-1])
    else:
        print("no functions found")
print(function_list)
find_function(func_declaration_1, js_file)
find_function(func_declaration_2, js_file)"""

