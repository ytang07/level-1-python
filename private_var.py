class Shape:
    def __init__(self, sides):
        self.sides = sides
    
    def name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

triangle = Shape(3)
triangle.name("t1")
print(triangle.get_name())
print(triangle.sides)
print(triangle.__name)
