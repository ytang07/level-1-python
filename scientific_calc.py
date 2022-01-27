import math

# create function declarations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a/b

def multiply(a, b):
    return a*b

def square(a):
    return a**2

def sqrt(a):
    return math.sqrt(a)

def log(a):
    return math.log(a)

def exponentiate(a, b):
    return a**b

# create map
function_map = {
    "add": add,
    "subtract": subtract,
    "divide": divide,
    "multiply": multiply,
    "square": square,
    "square root": sqrt,
    "log": log,
    "exponentiate": exponentiate
}

# ask user for desired operation
op = input("Which operation would you like to do? Add, subtract, divide, multiply, square, square root, log, or exponentiate? ")
if op in ["square", "square root", "log"]:
    a = float(input("What number would you like to perform your operation on? "))
    x = function_map[op](a)
    print(x)
else:
    a = float(input("What is the first number? "))
    b = float(input("What is the second number? "))
    x = function_map[op](a, b)
    print(x)