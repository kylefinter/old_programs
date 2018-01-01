'''
Program that needs a lock
'''
import threading

total = 0

def update_total(amount):
    '''Updates total by given amount'''
    global total
    lock = threading.RLock()
    lock.acquire()
    with lock:
        total += amount
    lock.release()
    print(total)

if __name__ == "__main__":
    for i in range(10):
        t = threading.Thread(target = update_total, args = [5])
        t.start()
