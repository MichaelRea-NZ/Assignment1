import re

js_file = "class Rectangle {constructor(height, width) {this.height = height;\
               this.width = width;} get area(){return this.calcArea();}   calcArea()\
               {return this.height * this.width; }}const square = new Rectangle\
               (10, 10);console.log(square.area);"
print(js_file)

def find_class(js_file)
    class_name_finder = re.match(r'^class.(\w+)', js_file)
    if class_name_finder is not None:
         # print(class_name_finder.group())
         #print(class_name_finder.group().split())
        print(class_name_finder.group().split()[-1]+'\n')
        class_name = class_name_finder.group().split()[-1]
        print(class_name)
   
function_list = []

def find_function_1(js_file):
    func_declaration_1 = re.findall(r'^function.(\w+)', js_file)
    if find_function_1 is not None:
        function_list.append(func_declaration_1.group().split()[-1])
        print(function_list)


def find_function_2(func, js_file):
        func_declaration_2 = re.findall(r' \w+ ?=[= (.+) =>]', js_file)
        if find_function_2 is not None:
            function_list.append(func_declaration_2.group().split()[-1])
            print(function_list)
