import math
def zero(num, x) :
    temp = x
    sum = 0
    while temp<=2000000000 :
        sum += num//temp
        temp *= x
    return sum

N, K = map(int, input().split())

if K < 0 or K>N :
    print(0)
    
else :
    a = zero(N,5) - zero(K,5) - zero(N-K,5)
    b = zero(N,2) - zero(K,2) - zero(N-K,2)
    print(min(a,b))
    
