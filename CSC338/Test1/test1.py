'''
Kyle Finter
Calculate a global sum using multiple processes
'''
import sys
import multiprocessing
from multiprocessing import Process, Queue

def readfile(fname):
    '''Reads a text file; returns a list of integers'''
    f = open(fname, 'r')
    contents = f.read()
    numbers = contents.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    return numbers

def subtotal(alist, result):
    '''Add the correct arguments to calculate the total of a list of numbers'''
    result.put(sum(alist))
    return

def main(num_processes):
    fname = "randnums.txt"
    numlist = readfile(fname)  #numlist is a list of integers
    workload = len(numlist)/num_processes
    listOfList = [[] for _ in range(num_processes)]
    count=-1
    listNum=0
    for x in numlist:
        if(count<workload-1):
            listOfList[listNum].append(x)
            count=count+1
        else:
            listNum=listNum+1
            listOfList[listNum].append(x)
            count=0
    #Your code here to determine which numbers from numlist to send
    #to each process, start the processes, get the subtotals, calculate
    #the global sum, and print the global sum
    processList = []
    results=[]
    res = Queue()
    for i in range(num_processes):
        p = Process(target = subtotal, name = "process "+str(i), args = [listOfList[i], res])
        processList.append(p)
        p.start()
    for p in processList:
        p.join()
    for x in range(num_processes):
        results.append(res.get())
    globalSum = sum(results)
    print("The global sum is "+str(globalSum))

if __name__ == "__main__":
    num_processes = int(sys.argv[1])
    main(num_processes)
