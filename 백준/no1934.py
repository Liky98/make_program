def firstTest(a,b) :
    if a<b :
        temp = a
        for i in range(a) :
            if b%temp == 0 and a%temp == 0:
                break
            else :
                temp -= 1
    else :
        temp = b
        for i in range(b) :
            if b%temp == 0 and a%temp == 0:
                break
            else :
                temp -= 1
    return temp

def secondTest(a,b,x) :
    print(a*b//x)

T = int(input())

for i in range(T) :
    a, b = map(int,input().split())
    secondTest(a,b,firstTest(a,b))

