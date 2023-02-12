def longword(filename):
    maxlen=0
    maxword=''
    f=open(str(filename),'r')
    text=f.read()
    words=text.split()
    for j in words:
        if len(j)>maxlen:
            maxlen=len(j)
            maxword=j
    return maxword
# def longword():
#     maxlen=0
#     maxword=''
#     f=open('name.txt','r')
# 	  i=f.read()
#     words=i.split()
#     for j in words:
#         if len(j)>maxlen:
#             maxlen=len(j)
#             maxword=j
#     return maxword>>>>>this function is only for one text file.
# while True:
ask=input('Enter text file name: ')
print('longest word is:',longword(ask))#,'\n'