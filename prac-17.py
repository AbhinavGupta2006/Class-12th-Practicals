import pickle
def createbinary():
    f=open('binsearch.txt','wb')
    n=int(input('Number of data: '))
    d={}
    for i in range(n):
        itemnumber=int(input('Enter item no.: '))
        itemname=input('Enter item name: ')
        price=int(input('enter price: '))
        d[itemnumber]=[itemname,price]
    pickle.dump(d,f)
    f.close()

def searchbinary(itemno):
    f=open('binsearch.txt','rb')
    try:
        while f:
            data=pickle.load(f)
            for i in data:
                if i==itemno:
                    print(i,data[i][0],data[i][1])
                    break
    except:
        f.close()
while True:
    ask=input('[C]reate or [S]earch: ')
    if ask.upper()=='C':
        createbinary()
    elif ask.upper()=='S':
        itemNo=int(input('Enter item no.: '))
        searchbinary(itemNo)