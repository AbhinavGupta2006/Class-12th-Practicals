n=int(input('Enter number of elements for tuple: '))
t=[]
for i in range (n):
    elem=int(input('Enter number: '))
    t.append(elem)
t=tuple(t)
def OddEvenTup(Tuple):
    odd=0
    even=0
    for i in range(len(Tuple)):
        if Tuple[i]%2==0:
            even+=1
        elif Tuple[i]%2==1:
            odd+=1
    print('Even numbers=',even)
    print('Odd numbers=',odd)
OddEvenTup(t)