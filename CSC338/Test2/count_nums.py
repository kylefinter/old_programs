#Prints number of numbers in a file and their total

fname = "randnums500.txt"

def readfile(fname):
    f = open(fname, 'r')
    nums = f.read()
    f.close()
    return nums

def main():
    nums = readfile(fname)
    num_list = nums.split()
    total = 0
    for num in num_list:
        total += int(num)
    print(len(num_list), total)

main()
