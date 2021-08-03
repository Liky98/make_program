import sys
import collections
import numpy as np



T = int(sys.stdin.readline())
for _ in range(T) :
    FuncArray = sys.stdin.readline()
    n = int(sys.stdin.readline())
    inputArray = sys.stdin.readline()[1:-2].split(",")
    deque = collections.deque(inputArray)

    for i in FuncArray :
        if i == "R" :
            deque.reverse()
        else :
            if len(deque) == 0 :
                print("error")
            else :
                deque.popleft()

    print(deque) 