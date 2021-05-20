def fac(num) :
    temp =1
    for i in range(1,num+1) :
        temp *= i
        
    return temp


def fac1(num) :
    if num==1 : return 1
    return num*fac1(num-1)

T = int(input())
for i in range(T) :
    b, a = map(int, input().split())
    x= fac(a-b)*fac(b)
    y = fac(a) 
    print(y//x)