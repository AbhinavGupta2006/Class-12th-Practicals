StackVow=[]
def Stack_push():
    n=int(input('Number of elements: '))
    for i in range(n):
        item=input('Enter vowel: ')
        StackVow.append(item)
    print(StackVow)
def Stack_pop():
    for i in range(len(StackVow)-1,-1,-1):
        print(StackVow[i],end=' ')
while True:
    ask=int(input('\n1. Push\n2. POP\n'))
    if ask==1:
        Stack_push()
    elif ask==2:
        Stack_pop()