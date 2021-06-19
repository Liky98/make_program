arrayList = []

def puts(num) :
    arrayList.append(num)

def pops() :
    arrayList.pop()

# def numberSum() :
#     for a in arrayList :
#         sumNum22 = sumNum22 + a
#     print(sumNum22)


T = int(input())
for i in range(T):
    number = int(input())
    if number != 0 :
        puts(number)
    else :
        pops()

    if i == T-1:
        print(sum(arrayList))