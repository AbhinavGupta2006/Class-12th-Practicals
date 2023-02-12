import pickle
def createbinary():
    f=open('binsearch.txt','wb')
    n=int(input('Number of data: '))
    d={}
    for i in range(n):
        Roll=int(input('Enter Roll no.: '))
        Name=input('Enter name: ')
        marks=int(input('enter marks: '))
        d[Roll]=[Name,marks]
    pickle.dump(d,f)
    f.close()

def updatebinary(roll):
    f=open('binsearch.txt','rb+')
    pos=0
    try:
        while f:
            data=pickle.load(f)
            print(data)
            for i in data:
                if i==roll:
                    f.seek(pos)
                    data[roll][1]=int(input('Enter marks to update: '))
                    pickle.dump(data,f)
                    break
                else:
                    pos=f.tell()
            else:
                print('roll number invalid')
            print(data)
    except:
        f.close()

while True:
    ask=input('[C]reate or [U]pdate: ')
    if ask.upper()=='C':
        createbinary()
    elif ask.upper()=='U':
        roll=int(input('Enter roll: '))
        updatebinary(roll)
    # elif ask.upper()=='D':
    #     f=open('binsearch.txt','rb')
    #     try:
    #         while f:
    #             d=pickle.load(f)
    #     except:
    #         print(d)
    #         f.close()