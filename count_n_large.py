import sys
import timeit
import heapq
import time


def count_1(file,n):
    result_list = ['']*n
    writer = open('largest_%s.txt'%n, 'w')
    for line in file:
        if len(line.strip()) > len(result_list[-1]):
            result_list = insert(line.strip(), result_list)
    writer.write('\n'.join(result_list))
    writer.close()

def insert(item, input_list):
    for idx,line in enumerate(input_list[:-1]):
        if len(item)>len(line):
            return input_list[:idx]+[item]+input_list[idx:-1] if idx else [item]+input_list[idx:-1]
    return input_list[:-1]+[item]

def count_2(file, n):
    lines = file.readlines()
    writer = open('largest_count2_%s.txt'%n, 'w')
    writer.write(''.join(heapq.nlargest(n, lines, len)))


if __name__ =='__main__':
    s_time = time.time()

    count_1(open(sys.argv[1],'r'), int(sys.argv[2]))

    end_time = time.time()
    print (end_time-s_time)

    s_time = time.time()

    count_2(open(sys.argv[1],'r'), int(sys.argv[2]))

    end_time = time.time()
    print (end_time-s_time)
