"""f=open('textfile.txt','r')
f1=open('textfilewitha.txt','a')
for i in f:
    if 'a' in i:
        f1.write(i)
f.close()
f1.close()"""


f=open('textfile.txt','r')
f1=open('textfilewitha.txt','a')
fl=f.readlines()
for i in fl:
    if 'a' in i:
        f1.write(i)
        fl.remove(i)
f.close()
f=open('textfile.txt','w+')
for j in fl:
    f.write(j)
print('done')
f.close()
f1.close()