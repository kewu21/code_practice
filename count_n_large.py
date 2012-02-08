import sys
import heapq
import time


def count_1(file,n):
    ''' This first function using a insertion-sort kind of method to get the
        N largest line into a sorted list.
        This algorithm is suitalbe for large file size with small n, since
        it evalutes each line as it reads it. So it won't requir much extra
        space.
    '''
    #initialize a empty list with n length in order to hold the N largest
    #sentences in the file
    result_list = ['']*n

    writer = open('largest_%s.txt'%n, 'w')
    for line in file:
        #for every line in the file, if the length of the line is greater
        #than the shortest line in the list, replace the shortest one with
        #this line, than insert the new line into proper position
        if len(line) > len(result_list[-1]):
            result_list = insert(line, result_list)
    #write the result to a new file
    writer.write(''.join(result_list))
    writer.close()

def insert(item, input_list):
    for idx,line in enumerate(input_list[:-1]):
        #find the position for new line, then insert it
        if len(item)>len(line):
            return input_list[:idx]+[item]+input_list[idx:-1] if idx else [item]+input_list[idx:-1]
    return input_list[:-1]+[item]

def count_2(file, n):
    ''' This function using heap data structure, O(k*log(n)) time complexity
        is every effcient for a large n. However, when encoutner a very
        large file, it needs much more space since a list is created to
        store the whole file
    '''
    lines = file.readlines()
    writer = open('largest_count2_%s.txt'%n, 'w')
    writer.write(''.join(heapq.nlargest(n, lines, len)))
    writer.close()


if __name__ =='__main__':
    '''
        To use this module, type pyton count_n_largest.py <filename> <rank>
        on command line
    '''
    count_1(open(sys.argv[1],'r'), int(sys.argv[2]))
    count_2(open(sys.argv[1],'r'), int(sys.argv[2]))
