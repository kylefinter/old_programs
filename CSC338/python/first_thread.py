import threading
import time

def fun1(i,j):
    """Executes inside a thread"""
    print("hello from a thread!")
    print(threading.currentThread().getName())
    print(__name__)
    print(i,j)
    time.sleep(1)
    print("Goodbye from a thread!")
    return

def fun2(i,j):
    print("hello from", threading.currentThread().getName())
    time.sleep(2)
    return

def fun3(i,j):
    print("hello from", threading.currentThread().getName())
    time.sleep(3)
    return

if __name__ == "__main__":
    t1 = threading.Thread(target = fun1, name = "fun1", args = [42,38]) #Create a thread object
    t1.start()  #Start the thread
    t2 = threading.Thread(target = fun2, name = "fun2", args = [42,38]) #Create a thread object
    t2.start()  #Start the thread
    t3 = threading.Thread(target = fun3, name = "fun3", args = [42,38]) #Create a thread object
    t3.start()  #Start the thread
