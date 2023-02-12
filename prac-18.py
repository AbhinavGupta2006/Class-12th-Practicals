import csv
f=open("a.csv","a",newline='')
csvw=csv.writer(f)
data=["NAME","ROLL NO."]
csvw.writerow(data)
n=int(input("How many records? "))
for i in range(n):
    name=input("Enter name: ")
    rno=input("Enter roll no.: ")
    l=[name,rno]
    csvw.writerow(l)
f.close()
f=open("a.csv","r")
R=input("Enter Roll no to be searched: ")
csvr=csv.reader(f)
for i in csvr:
    if i[1]==R:
        print(i[0])
        break
else:
    print('NO such roll number!')
f.close()