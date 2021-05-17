import math
def test(mainNum, subNum) :
    x = math.gcd(mainNum, subNum)
    print("{0}/{1}".format(mainNum//x, subNum//x))

T = int(input())
array = list(map(int, input().split()))
for i in array :
    if i == array[0] : continue
    test(array[0], i)