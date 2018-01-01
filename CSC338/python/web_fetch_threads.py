import threading
import urllib.request as req
import time
import queue

hosts = ["http://missouri.edu/", "http://www.missouristate.edu/",
         "http://www.mssu.edu/", "http://www.semo.edu/",
         "http://umkc.edu", "http://mst.edu", "https://www.ucmo.edu/",
         "http://www.umsl.edu/", "http://www.truman.edu/",
         "http://www.nwmissouri.edu/"]

#get web pages from hosts and print first 50 characters
def get_page(host):
    cur = host.get()
    #for host in hosts:
    url = req.urlopen(cur)
    html = url.read()
    print(cur, html[:50])
    host.task_done()

def main():
    que = queue.Queue()
    #que.put(hosts)
    for host in hosts:
        que.put(host)
    for i in range(len(hosts)):
        t = threading.Thread(target = get_page, name = "gp"+str(i), args = [que])
        t.start()
        t.join()
    que.join()
    #get_page(hosts)

start = time.time()
main()
print("Elapsed time: %s" % (time.time() - start))
