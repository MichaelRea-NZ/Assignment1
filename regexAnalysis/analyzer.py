import re

js_file = "class Rectangle {constructor(height, width) {this.height = height;\
               this.width = width;} get area(){return this.calcArea();}   calcArea()\
               {return this.height * this.width; }}const square = new Rectangle\
               (10, 10);console.log(square.area);"
print(js_file)
class_name_finder = re.search("class: (\w+)", js_file)
print(class_name_finder.groups())
