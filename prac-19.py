import csv
f=open("b.csv","a",newline='')
csvw=csv.writer(f)
data=['Itemnumber','Itemname','Price']
csvw.writerow(data)
n=int(input("How many records? "))
for i in range(n):
    I_no=input("Enter Item number: ")
    I_name=input("Enter Item name: ")
    I_price=input('Enter Item price:')
    l=[I_no,I_name,I_price]
    csvw.writerow(l)
f.close()
f=open("b.csv","r")
I=input("Enter Item number to be searched: ")
csvr=csv.reader(f)
for i in csvr:
    if i[0]==I:
        print(i[0],i[1],i[2])
        break
f.close()