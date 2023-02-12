import pickle

def theinput():
    f=open('binsearch.txt','wb')
    n=int(input('Number of data: '))
    d={}
    for i in range(n):
        Roll=int(input('Enter Roll no.: '))
        Name=input('Enter name: ')
        d[Roll]=Name
    pickle.dump(d,f)
    f.close()

def searc(roll):
    f=open('binsearch.txt','rb')
    try:
        while f:
            data=pickle.load(f)
            print(data[roll])
    except:
        f.close()
while True:
    
    ask=input('[I]nput or [S]earch:')
    if ask == 'i':
        theinput()
    elif ask == 's':
        w=int(input('Enter roll: '))
        searc(w)

    # r=int(input('Enter roll no: '))
    # searc(r)