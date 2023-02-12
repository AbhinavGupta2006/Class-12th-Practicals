def OElist(listmain):
    for i in range(len(listmain)):
        if listmain[i]%2==0:
            listmain[i]=listmain[i]//2
        elif listmain[i]%2==1:
            listmain[i]=listmain[i]*2
    return listmain
l=eval(input("Enter the list: "))
print("The odd values are doubled and the even values are halved\n",OElist(l))