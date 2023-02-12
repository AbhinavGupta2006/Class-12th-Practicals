a=open('Thefile.txt','r')
f=True
while f:
    l=a.readline()
    if not l:
        f=False
    l=l.replace(' ','#')
    l=l.replace('\n',' ')
    print(l)
a.close()