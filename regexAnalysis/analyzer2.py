import re


class Analyzer:
    def __init__(self):
        #TODO make up scripts to test function declerations
        self.js_file = " Rectangle class constructor (height, width) {this.height = height;\
                this.width = width;} get class area(){return this.calcArea();}  \
               calcArea() { function return this.height * this.width; }}const square = \
               function new Rectangle (10, 10);console.log(square.area);"

    def find_class(self):
        #  class_name_finder = re.match(r'^class.(\w+)', self.js_file)
        class_name_finder = re.search(r'class.(\w+)', self.js_file)
        if class_name_finder is not None:
            class_name = class_name_finder.group().split()[-1]
            print(class_name)
            #self.find_class(class_name_finder, self.js_file)


# def find_class(func, js_file):
#     print(js_file)
#     class_name_finder = re.match(r'^class.(\w+)', js_file)
#     if class_name_finder is not None:
#         print(class_name_finder.group().split()[-1] + '\n')
#         class_name = class_name_finder.group().split()[-1]
#         print(class_name)
#
#         find_class(class_name_finder, js_file)

    def find_function_1(self):
        #TODO make findall() read though multipile lines
        func_declaration_1 = re.findall(r'function.(\w+)',self.js_file)
        if func_declaration_1 is not None:
            function_name = func_declaration_1
            #function_list.append(func_declaration_1.group().split()[-1])
            print(function_name)


    def find_function_2(self):
        func_declaration_2 = re.findall(r'\w+ ?=[=\\.+)=>]', self.js_file)
        if func_declaration_2 is not None:
            function_name =func_declaration_2
            print(function_name)



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
