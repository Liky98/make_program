from math import gcd, sqrt

#입력받고 내림차순 정렬
T = int(input())
array = [input() for i in range(T)]
array= list(map(int, array))
array.sort(reverse=True)

#a-b, b-c ... 이런식으로 나온 값들 개별로 최대공약수 저장
answer = list()
for i in range(1, len(array)) :
  x = array[i] - array[i-1]
  answer += [(gcd(x))]

#최대공약수 저장한 배열에서 두개씩 묶어서 모든 객체의 최대공약수 구함
for i in range(1,len(answer)):
      answer[i] = gcd(answer[i], answer[i-1])

#마지막 배열에 저장되어있는게 모든 배열의 최대공약수임
x = int(answer[-1])

#새로운 리스트 생성 및 시간절약을 위해 절반까지만 돌면서 최대공약수의 약수를 리스트에 저장
a=[]
for i in range(2, int(sqrt(x)) + 1):
    if x % i == 0:
        a.append(i)
        a.append(x // i)
a.append(x)

#중복 숫자 제거를 위한 set으로 리스트 만듬
a = list(set(a))

#오름차순으로 정렬함
a.sort()

#하나씩 출력
for i in a:
    print(i, end = ' ')
