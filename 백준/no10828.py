
def push(num):
    arrayList.append(num)

def pop() :
    if len(arrayList) == 0 :
        print(-1)
    else :
        print(arrayList.pop())

def size() :
    print(len(arrayList))

def empty() :
    if len(arrayList) == 0 :
        print(1)
    else :
        print(0)

def top() :
    if len(arrayList) == 0 :
        print(-1)
    else :
        print(arrayList[-1])

import sys

arrayList = []
T = int(input())
for i in range(T) :
    # a, b = list(map(str, input().split()))
    N = sys.stdin.readline().rstrip().split()
    a = N[0]
    if a == "push" :
        push(N[1])
    elif a == "pop" :
        pop()
    elif a == "size" :
        size()
    elif a == "empty" :
        empty()
    elif a == "top" :
        top()
