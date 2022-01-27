import matplotlib.pyplot as plt
import random

# function 1 - generate dataset
def gen():
    x = [random.uniform(0, 1) for _ in range(25)]
    x.sort()
    y = [2*_x for _x in x]
    return x, y

# function 2 - plot generated dataset
def plot(x: list, y: list):
    plt.plot(x, y)
    plt.title("plotting a generated dataset")
    plt.show()

# function 3 - tie them together
def orchestrate():
    x, y = gen()
    plot(x, y)
    
orchestrate()