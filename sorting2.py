########################################################################
def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return None
    
########################################################################
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
        
def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        # invariant: ``seq[:i]`` is sorted        
        # find the least `low' such that ``seq[low]`` is not less then `key'.
        #   Binary search in sorted sequence ``seq[low:up]``:
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1             
            else:
                up = middle
        # insert key at position ``low``
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]
        
########################################################################
def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i,len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst

########################################################################
from heapq import merge
  
def merge_sort(m):
    if len(m) <= 1:
        return m
  
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
  
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))
    
########################################################################
def swap(i, j):                    
    list[i], list[j] = list[j], list[i] 
 
def heapify(end,i):   
    l=2 * i + 1 
    r=2 * (i + 1)   
    max=i   
    if l < end and list[i] < list[l]:   
        max = l   
    if r < end and list[max] < list[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   
 
def heap_sort():     
    end = len(list)   
    start = end // 2 - 1
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0)

########################################################################
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more                                    

########################################################################
import time
from random import shuffle
 
def main(): 
	nitems=5000
 
	numbs=[i for i in range(nitems)]
	shuffle(numbs)
	start=time.clock()
	bubble_sort(numbs)
	end = time.clock()
	print('Bubble', end-start, "seconds")
	
	numbs=[i for i in range(nitems)]
	shuffle(numbs)
	start=time.clock()
	selection_sort(numbs)
	end = time.clock()
	print('SelectionSort', end-start, "seconds")
	
	numbs=[i for i in range(nitems)]
	shuffle(numbs)
	start=time.clock()
	insertion_sort(numbs)
	end = time.clock()
	print('InsertionSort', end-start, "seconds")
	
	numbs=[i for i in range(nitems)]
	shuffle(numbs)
	start=time.clock()
	merge_sort(numbs)
	end = time.clock()
	print('MergeSort', end-start, "seconds")
	
	numbs=[i for i in range(nitems)]
	shuffle(numbs)
	start=time.clock()
	quickSort(numbs)
	end = time.clock()
	print('QuickSort', end-start, "seconds")

main()
