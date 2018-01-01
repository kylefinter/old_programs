import threading
import urllib.request as req
import time
import queue
import multiprocessing as mp

hosts = ["http://missouri.edu/", "http://www.missouristate.edu/",
         "http://www.mssu.edu/", "http://www.semo.edu/",
         "http://umkc.edu", "http://mst.edu", "https://www.ucmo.edu/",
         "http://www.umsl.edu/", "http://www.truman.edu/",
         "http://www.nwmissouri.edu/"]

#get web pages from hosts and print first 50 characters
def get_page(que, host1, host2):
    #cur = host.get()
    url = req.urlopen(host1)
    html = url.read()
    print(host1, html[:50])
    url = req.urlopen(host2)
    html = url.read()
    print(host2, html[:50])
    que.task_done()

def main():
    que = queue.Queue()
    processes = []
    for host in hosts:
        que.put(host)
    for i in range(len(hosts)):
        if i % 2 == 0:
            p = mp.Process(target = get_page, args = [que, que.get(), que.get()])
            processes.append(p)
            p.start()
    for p in processes:
        p.join()

start = time.time()
main()
print("Elapsed time: %s" % (time.time() - start))
