def listSum(list):
    sum=0
    for i in list:
        sum+=int(i)
    return sum
L=eval(input('Enter the list: '))
print(listSum(L))