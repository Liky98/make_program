while True :
    x = input()
    if x == '.' : 
        break
    list = []
    tf = True
    for i in x :
        if i == '[' or i == '(' :
            list.append(i)

        elif i == ']' :
            if len(list) == 0 or list[-1] != '[':
                tf = False
                break
            list.pop(-1)
        elif i == ')' :
            if len(list) == 0 or list[-1] != '(':
                tf = False
                break
            list.pop(-1)
    if tf and len(list) ==0: 
        print("yes")
    else : 
        print("no")