
def test(num01, num02) :
    if num02 % num01 == 0 :
        print("factor")
    elif num01 % num02 == 0:
        print("multiple")
    else :
        print("neither") 
        

while True :
    number01, number02 = map(int, input().split())
    if number02 == 0 and number01==0 :
        break
    test(number01, number02)
    
