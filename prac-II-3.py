R={"OM":76, "JAI":45, "BOB":89, "ALI":65, "ANU":90, "TOM":82}
stack=[]
def Push_d():
    for i in R:
        if R[i]>75:
            stack.append(i)
def Pop_d():
    for i in range(len(stack)-1,-1,-1):
        print(stack[i],end=' ')
Push_d()
Pop_d()