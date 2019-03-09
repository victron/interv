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
            


# max number of same letters
# st = 'aaaabbbccaaaaaaccfd' sequences could repeated

def max_sequence(st: str)-> int:
    if len(st) == 1:
        return 1
    previous = st[0]
    count = 1
    max_count = 0
    for i in st[1:]:
        if i != previous:
            previous = i
            count = 1
            continue
        if i == previous:
            count += 1
        if max_count < count:
            max_count = count
    
    return max_count

    
