import sys
import collections 

def first() :
    array.popleft()

def second() :
    global count
    temp = array.popleft()
    array.append(temp)
    count += 1

def third() :
    global count
    temp = array.pop()
    array.appendleft(temp)
    count += 1
    
count = 0

n, m = map(int, sys.stdin.readline().split())
sequnceArray = list(map(int, sys.stdin.readline().split()))

array = collections.deque(_ for _ in range(1,n+1))

for i in sequnceArray :
    while i != array[0] :
        if array.index(i) < len(array)/2 :
            second()
        else :
            third()
    first()

print(count)
#