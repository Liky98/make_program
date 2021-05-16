from math import gcd, sqrt

T = int(input())
array = [input() for i in range(T)]
array= list(map(int, array))
array.sort(reverse=True)

answer = list()
for i in range(1, len(array)) :
  x = array[i] - array[i-1]
  answer += [(gcd(x))]

for i in range(1,len(answer)):
      answer[i] = gcd(answer[i], answer[i-1])

x = int(answer[-1])

a=[]
for i in range(2, int(sqrt(x)) + 1):
    if x % i == 0:
        a.append(i)
        a.append(x // i)
a.append(x)

a = list(set(a))

a.sort()

for i in a:
    print(i, end = ' ')
