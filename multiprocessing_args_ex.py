from multiprocessing import Process

def func1(counter: int):
    print("start func 1")
    for i in range(100):
        counter += 1
        print("func 1", counter)
    print("end func 1")
    return counter

def func2(counter: int):
    print("start func 2")
    for i in range(100):
        counter += 1
        print("func 2", counter)
    print("end func 2")
    return counter

if __name__ == "__main__":
    counter1 = 0
    counter2 = 0
    p1 = Process(target = func1, args=(counter1,))
    p2 = Process(target = func2, kwargs={"counter":counter2})
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(p1)
    print(type(p1))