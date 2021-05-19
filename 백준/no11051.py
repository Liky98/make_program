def fac1(num) :
    if num==1 : return 1
    return num*fac1(num-1)

def fac2(num) :
    temp =1
    for i in range(1,num+1) :
        temp *= i
    return temp

N, K = map(int, input().split())

if K < 0 or K>N :
    print(0)
    
else :
    print((fac2(N) // (fac2(K)*fac2(N-K)))%10007)
