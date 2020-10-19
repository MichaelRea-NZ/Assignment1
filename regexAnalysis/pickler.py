import re


class Analyzer:
    def __init__(self, file_content):
        self.js_file = file_content

    def find_class(self):
        global class_name
        try:
            class_name = re.search(r'class.(\w+)', self.js_file)
            if self.js_file == '':
                raise Exception
        except Exception as e:
            print('A JS file needs to be selected to run the analyzer')
        else:
            if class_name is not None:
                class_name = class_name.group().split()[-1]
                print(class_name)

    def find_property(self):
        global property_name
        try:
            property_name = re.findall(r'this.(\w+)', self.js_file)
            if self.js_file == '':
                raise Exception
        except Exception as e:
            print('A JS file needs to be selected to run the analyzer')
        else:
            if property_name is not None:
                first_list = property_name
                print(first_list)
                first_list = [i.lower() for i in first_list]
                property_name = list(dict.fromkeys(first_list))
                property_name = (['{}\l'.format(i) for i in property_name])
                property_name = " ".join(property_name)
                print(property_name)

    def find_function_1(self):
        global function_name
        try:
            function_name = re.findall(r'function.(\w+)', self.js_file)
            if self.js_file == '':
                raise Exception
        except Exception as e:
            print('A JS file needs to be selected to run the analyzer')
        else:
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
 {class_name}[ label = " {{{class_name}| {property_name}|{function_name}\
}}"]}}')
        dot_file1.close()
        dot_file1 = open("classfile.dot", "r")
        print(dot_file1.read())
