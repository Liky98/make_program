s = []
outputList = []
temp = True

count = 1
for i in range(int(input())):
    num = int(input())
    while count <= num:
        s.append(count)
        outputList.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        outputList.append('-')
    else:
        temp = False
        
if temp == False:
    print('NO')
else:
    for i in outputList:
        print(i)
