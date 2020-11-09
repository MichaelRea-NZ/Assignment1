import re


class Analyzer:
    def __init__(self, file_content):
        self.js_file = file_content
        self.class_name = ""
        self.property_name = ""
        self.function_name = ""
        self.dot_file1 = ""

    def find_class(self):
        # global class_name
        try:
            self.class_name = re.search(r'class.(\w+)', self.js_file)
            if self.js_file == '':
                raise Exception
        except Exception as e:
            print('A JS file needs to be selected to run the analyzer')
        else:
            if self.class_name is not None:
                self.class_name = self.class_name.group().split()[-1]
                print(self.class_name,'a')

    def get_class_name(self):
        return self.class_name

    def find_property(self):
        #global property_name
        try:
            self.property_name = re.findall(r'this.(\w+)', self.js_file)
            if self.js_file == '':
                raise Exception
        except Exception as e:
            print('A JS file needs to be selected to run the analyzer')
        else:
            if self.property_name is not None:
                first_list = self.property_name
                print(first_list)
                first_list = [i.lower() for i in first_list]
                self.property_name = list(dict.fromkeys(first_list))
                self.property_name = (['{}\l'.format(i) for i in self.property_name])
                self.property_name = " ".join(self.property_name)
                print(self.property_name,'a' )

    def get_property_name(self):
        return self.property_name


    def find_function_1(self):
        #global function_name
        try:
            self.function_name = re.findall(r'function.(\w+)', self.js_file)
            if self.js_file == '':
                raise Exception
        except Exception as e:
            print('A JS file needs to be selected to run the analyzer')
        else:
            if self.function_name is not None:
                self.function_name = self.function_name
                self.function_name = (['{}()\l'.format(i) for i in self.function_name])
                self.function_name = " ".join((self.function_name))
                print(self.function_name)

    def get_function_name(self):
        return self.function_name

    def get_no_file(self):
        if self.js_file =='':
            return 'A JS file needs to be selected to run the analyzer'

    def create_file(self):
        self.dot_file1 = open("classfile.dot", "w")
        self.dot_file1.write(f'digraph G {{fontname = "Bitstream Vera Sans"\
fontsize = 8 node [fontname = "Bitstream Vera Sans"\
fontsize = 8 shape = "record"]\
edge [fontname = "Bitstream Vera Sans"fontsize = 8] {self.class_name}\
[ label = " {{{self.class_name}|{self.property_name}|{self.function_name}\
}}"]}}')
        self.dot_file1.close()
        self.dot_file1 = open("classfile.dot", "r")
        print(self.dot_file1.read())
        self.dot_file1.close()
        #print(self.class_name)

    # def do_get_create_file(self):
    #     self.dot_file1 = open("classfile.dot", "r")
    #     result = print(self.dot_file1.read())
    #     return result
    #     print(result)

