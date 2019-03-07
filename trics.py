# swap two ints without copy in temp value
a = 3
b = 7

a = a + b
b = a - b
a = a - b
 

#  there is array values inside  from 1 till 100. array unsorted. need to find missing number
# without sorting
from random import shuffle

arr = list(range(100 + 1))
shuffle(arr)
missing_number = arr.pop()

def findMissing(arr):
    for i in range(100 + 1):
        if i not in arr:
            return i
            
