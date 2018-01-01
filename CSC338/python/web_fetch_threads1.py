#This program uses urllib to download web pages
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
def get_page(hosts):
    global que
    que = queue.Queue()
    que.put_nowait(hosts)
    #for host in hosts:
    #    que.put(host)
    for i in range(len(hosts)):
        t = threading.Thread(target = web_page, name = "gp"+str(i), args = [que.get()])
        t.start()
    #for host in hosts:
    #    t1 = threading.Thread(target = web_page, name = "web_page_host", args = [host]) #Create a thread object
    #    t1.start()  #Start the thread
    que.join()

def web_page(page):
    url = req.urlopen(page)
    html = url.read()
    print(page, html[:50])
    return

def main():
    get_page(hosts)

start = time.time()
main()
print("Elapsed time: %s" % (time.time() - start))
