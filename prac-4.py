def nfibo(n):
    n1=1
    n2=1
    n3=0
    if n==1 or n==2:
        return 1
    for i in range(n-2):
        n3=n1+n2
        n1,n2=n2,n3
    return(n3)
while True:
    number=int(input("Enter the value of n for nth fibonacci number: "))
    print(nfibo(number))