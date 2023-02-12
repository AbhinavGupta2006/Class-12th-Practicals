def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
while True:
    ask=int(input("Enter a natural number to find factorial: "))
    if ask>0:
        print(factorial(ask))
