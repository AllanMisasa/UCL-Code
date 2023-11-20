import threading
from time import perf_counter

def myThread(func, args):
    t1_start = perf_counter()
    func(args)
    t1_stop = perf_counter()
    print("Elapsed time:", t1_stop - t1_start)

def myFunction(args):
    data = [args*args for args in range(10000000)]

def compareFunction(args):
    data = [args*args for args in range(20000000)]

def main():
    thread1 = threading.Thread(target=myThread, args=(myFunction, 5))
    thread2 = threading.Thread(target=myThread, args=(compareFunction, 5))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

main()