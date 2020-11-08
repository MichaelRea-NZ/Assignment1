import sys
import os
from cmd import Cmd
from analyzer import Analyzer
from PIL import Image
from pickler import Pickles


class GilliamPrompt(Cmd):
    doc_header = "Here are the list of commands in help.\n To get help on a " \
                 "command, enter 'help' followed by command name'."

    def __init__(self):
        Cmd.__init__(self)
        self.js_file_content = ""
        self.js_pickle_file = ""
        self.arg = ""

    def do_help_list(self, arg):
        """Enter 'help_list to see a list of all the commands in help """
        """and what they do."""
        print("analyzer\t\tEnter 'analyzer' to analysis the selected file.\n"
              "\ndraw\t\tEnter 'draw' to draw the selected file.\n"
              "\nhelp_list\t\tEnter 'help_list to see a list of all the "
              "commands in help and what they do.\n"
              "\nselect_file\t\tEnter 'select_file' to enter the file "
              "path of the JavaScript file that requires a UML diagram.\n"
              "\ndisplay\t\tEnter 'display' to view the drawing.\n"
              "\nshut\t\tEnter 'shut y' To leave the program.")

        def get_do_help_list(self):
            result = self.do_help_list(self)
            return self.do_help_list(self)
            print(result)

    def do_select_file(self, arg):
        """Enter 'select_file' to enter the file path of the JavaScript"""
        """file that requires a UML diagram """
        print('Enter the file path and file name of the file that ' +
              'requires analyzing')
        # call file opener
        if (arg.endswith(".js")):
            file_name = arg
            print('You selected ', file_name, "\n")
            self.open_file(file_name)
        else:
            print("The file is not a JavaScript file")

    def open_file(self, file_name):
        if file_name != '':
            try:
                file = open(file_name)
            except FileNotFoundError:
                print("The file does not exist at that location\n"
                      "Please check your file and try again")
            else:
                self.js_file_content = file.read()
                print("\n Hi", file_name, "\n")
                print(self.js_file_content)

    def do_analyse(self, arg):
        """Enter 'analyzer' to analysis the selected file."""
        analyzer = Analyzer(self.js_file_content)
        analyzer.find_class()
        analyzer.find_property()
        analyzer.find_function_1()
        analyzer.create_file()

    def do_draw(self, arg):
        """Enter 'draw' to draw the selected file."""
        os.system("Graphviz\\bin\\dot.exe  -Tpng -O classfile.dot")
        print("Drawing UML diagram")

    def do_display(self, arg):
        """Enter 'display' to view the drawing."""
        diagram = Image.open('classfile.dot.png')
        diagram.show()

    def do_pickle(self, arg):
        """Enter 'pickle' to save as a pickle file."""
        pickler = Pickles(self.js_file_content)
        pickler.create_pickle()

    def do_open_pickle(self, arg):
        """Enter 'open_pickle' to open the pickle file"""
        pickler = Pickles(self.js_file_content)
        pickler.open_pickle()

    def do_shut(self, args):
        """ Enter 'shut y' To leave the program."""
        if args == "y":
            sys.exit()
        else:
            print("Welcome back. Enter a command!")


if __name__ == '__main__':
    prompt = GilliamPrompt()
    prompt.prompt = '>->-> '
    prompt.cmdloop('\nWelcome to Gilliam the JS class diagram drawer.\
                    \nType help or ? for a list of commands')
