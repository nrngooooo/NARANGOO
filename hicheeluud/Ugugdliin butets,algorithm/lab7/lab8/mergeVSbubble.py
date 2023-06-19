from merge_sort import mergeSort
from bubble_sort import bubbleSort
import random 
import time

arr = [random.randint(0, 100000) for i in range(15000)]

startB = time.time()
a = bubbleSort(arr)
endB = time.time()

startM = time.time()
b = mergeSort(arr)
endM = time.time()



print("Bubble sort :" ,endB - startB, "seconds")
print("Merge sort :" , endM - startM, "seconds")