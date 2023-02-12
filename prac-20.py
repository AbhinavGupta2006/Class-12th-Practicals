import csv
f=open('user.csv','w',newline='')
fw=csv.writer(f)
d=['UID','PASS']
fw.writerow(d)
n=int(input('How many users? '))
for i in range(n):
    UID=input('Enter user id: ')
    PASSWD=input('Enter password: ')
    l=[UID,PASSWD]
    fw.writerow(l)
f.close()
f=open('user.csv','r')
fr=csv.reader(f)
U=input('Enter UID to search: ')
for i in fr:
    if i[0]==U:
        print('password : ',i[1])
        break
f.close()