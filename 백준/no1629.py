a, b, c = map(int, input().split())
temp = pow(a,b//2)
if b%2 == 0 :
    print(temp*temp%c)
else :
    print(temp*temp*a%c)

print(pow(a,b,c))