import sys
import collections

for _ in range(int(sys.stdin.readline())) :
    FuncArray = sys.stdin.readline() #RDD
    n = int(sys.stdin.readline()) #4
    inputArray = sys.stdin.readline()[1:-2].split(",") #1,2,3,4
    if inputArray[0] != '' :
        deque = collections.deque(inputArray) # deque[1,2,3,4]
    else :
        deque = collections.deque()

    
    leftcount= 0
    rightcount = 0
    error = False
    TF = True #TF == True > 리버스x,  TF == False > 리버스ㅇ

    for i in FuncArray : # i == R or D
        
        if i == 'R' : #리버스
            if TF == True : TF = False
            else : TF = True

        elif i == 'D' : #Drop
            if  len(deque) == 0 : #요소가 없으면
                error = True  #error 출력하고 리셋
                break
            else :
                if TF == True :
                    #leftcount +=1
                    deque.popleft()
                elif TF == False :
                    #rightcount +=1
                    deque.pop()

    if FuncArray.count('R') %2 != 0 : # 리버스가 홀수면 
        deque.reverse()

    if error :
        print("error")
    else :
        print("[",end="")
        for i in range(len(deque)):
            print(deque[i],end="")
            if i != len(deque)-1:
                print(",",end="")
        print("]")
