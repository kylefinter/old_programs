'''
Multiprocessing lock
'''
import multiprocessing as mp

def printer(item, lock):
    lock.acquire()
    try:
        for i in range(10):
            print(item)
    finally:
        lock.release()

if __name__ == "__main__":
    items = ["hello hello hello", "goodbye goodbye goodbye", 10]
    plist = []
    lock = mp.Lock()
    for item in items:
        plist.append(mp.Process(target = printer, args = [item, lock]))
    for p in plist:
        p.start()
