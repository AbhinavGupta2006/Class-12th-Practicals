# def dictUpdate(dictionary,Key,Value):
#     dictionary[Key]=Value    
d={}
n=int(input('How many elements in dictionary: '))
for i in range(n):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    d[key]=value
# while True:
#     ask=input("Enter key to update: ")
#     update=input('Enter the updating value')
#     dictUpdate(d,ask,update)>>>commented part stays in an infinite loop.OBVIOUSLY -_-
def dictUpdate():
    ask=input("Enter key to update: ")
    update=input('Enter the updating value: ')
    d[ask]=update
    print(d)
dictUpdate()