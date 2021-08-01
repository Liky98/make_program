from collections import deque
import sys

n = int(sys.stdin.readline())
array = deque()
for i in range(n) :
    array.append(i+1)

while len(array) != 1 :
    array.popleft()
    temp = array.popleft()
    array.append(temp)

print(array.pop())
