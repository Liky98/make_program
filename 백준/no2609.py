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


a, b = map(int,input().split())
x=firstTest(a,b)
print(x)
secondTest(a,b,x)
