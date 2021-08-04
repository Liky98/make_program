import sys
import collections
import numpy as np

T = int(sys.stdin.readline())
for _ in range(T) :
    FuncArray = sys.stdin.readline()
    n = int(sys.stdin.readline())
    inputArray = sys.stdin.readline()[1:-2].split(",")
    deque = collections.deque(inputArray)

    TF = True

    for i in FuncArray :
        if i == 'R' :
            if TF == True : TF = False
            else : TF = True
        else :
            if len(deque) == 0 :
                print("error")
                continue
            if TF == True :
                deque.popleft()
            elif TF == False :
                deque.pop()

    if FuncArray.count('R') %2 != 0 :
        deque.reverse()

    print(deque) 
    