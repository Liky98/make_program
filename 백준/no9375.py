
from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    s = []
    for j in range(n):
        a, b = input().split()
        s.append(b)
    num = 1
    result = Counter(s)
    print(result)
    for key in result:
        num *= result[key] + 1
    print(num - 1)

# import math

# T = int(input())
# array = []
# for i in range(T) :
#     x = int(input())
#     for j in range(x) :
#         array[i].append(input().split())

#     array[i].sort(key = lambda x: (x[1]))

#     tempStr = array[i][0][1]
#     count = 1
#     subSum = 0
#     for z in range(len(array[0])) :
#         if z == 0 : continue

#         if array[i][z][1] == tempStr :
#             if z == len(array[0])-1 and count !=1 :
#                 subSum += math.factorial(count)
#                 break
#             else : 
#                 count +=1
#                 continue

#         elif count == 1 :
#             tempStr = array[i][z][1]
#             continue
#         else :
#             subSum += math.factorial(count)
#             count = 1
#             tempStr = array[i][z][1]
#             continue
#     max = math.factorial(len(array[0]))
#     print(max - subSum +1)
        
# ##############################
# # def x :
    
# #     for a,b in array[0] :

# #         if firstPass == 0 : 
# #             firstPass +=1
# #             continue
        
# #         if b == tempStr :
# #             count += 1
# #             firstPass +=1
# #             continue
            
# #         elif count == 1 : 
# #             firstPass +=1
# #             continue
        
# #         else :
# #             subSum += math.factorial(count)
# #             firstPass +=1
# #             count = 1
# #             continue
        
# #         if firstPass == len(array[i])-1:
# #             subSum += math.factorial(count)
# #             break