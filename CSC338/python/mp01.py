#From Parallel Programming Cookbook, ch 3, p73
#Spawn a process
import multiprocessing as mp

def foo(i):
    print("Called function in process:", i, __name__)
    return

def foo2(i):
    print("2 Called function in process:", i, __name__)
    return

def main():
    Process_jobs = []
    print(__name__)
    for i in range(4):
        if i % 2 == 0:
            p = mp.Process(target = foo, args = [i])
            Process_jobs.append(p)
            p.start()
        else:
            p = mp.Process(target = foo2, args = [i])
            Process_jobs.append(p)
            p.start()
        #p.join()

if __name__ == "__main__":
    main()
