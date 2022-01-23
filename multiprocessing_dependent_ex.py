from multiprocessing import Process, Value

def func1(counter):
    print("start func 1")
    for i in range(100):
        counter.value += 1
        print("func 1", counter.value)
    print("end func 1")

def func2(counter):
    print("start func 2")
    for i in range(100):
        counter.value += 1
        print("func 2", counter.value)
    print("end func 2")

def func3(counter):
    p1 = Process(target=func1, args=(counter,))
    p2 = Process(target=func2, args=(counter,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"func3, {counter.value}")

def func4(counter):
    p1 = Process(target=func1, args=(counter,))
    p2 = Process(target=func2, args=(counter,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"func4, {counter.value}")

if __name__ =="__main__":
    counter = Value('d', 0)
    p1 = Process(target=func3, args=(counter,))
    p2 = Process(target=func4, args=(counter,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"main, {counter.value}")