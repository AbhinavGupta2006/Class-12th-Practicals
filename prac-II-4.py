N=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
stack=[]
def Push_S():
    for i in N:
        if i%2==0:
            stack.append(i)
def PopDisplay():
    for i in range(len(stack)-1,-1,-1):
        print(stack[i],end=' ')
Push_S()
PopDisplay()