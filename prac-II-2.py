student=[]
def Push_Stack():
    n=int(input('Number of records: '))
    for i in range(n):
        name=input('Enter name: ')
        marks=int(input('Enter marks: '))
        l=[name,marks]
        student.append(l)
    print(student)
def pop_stack():
    for i in range(len(student)-1,-1,-1):
        print(student[i],end=' ')
while True:
    ask=int(input('\n1.Push\n2.POP\n'))
    if ask==1:
        Push_Stack()
    elif ask==2:
        pop_stack()