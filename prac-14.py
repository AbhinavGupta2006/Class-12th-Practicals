def write(string):
    f=open('fileformenu.txt','a')
    f.write(string+'\n')
    f.close()
def nolines():
    f=open('fileformenu.txt','r')
    fr=f.read()
    count=fr.count('\n')
    f.close()
    return count
def char():
    f=open('fileformenu.txt','r')
    print('no of characters')
    n=1
    for i in f:
        i=i.replace(' ','')
        print('line',n,':',len(i)-1)
        n+=1
    f.close()
def words():
    f=open('fileformenu.txt','r')
    print('no of words')
    n=1
    for i in f:
        word=i.split()
        print('line',n,':',len(word))
        n+=1
    f.close()
def ser(word):
    f=open('fileformenu.txt','r')
    fr=f.read()
    occur=fr.count(str(word))
    return occur
while True:
    menu=input('(a) write contents into file\n\
(b) Display no of lines\n\
(c) Display no of characters in each line\n\
(d) Display no of words in each line\n\
(e) search a word\n')
    if menu=='a':
        ask=input('enter content for file:')
        write(ask)
    elif menu=='b':
        print('no of lines:',nolines())
    elif menu=='c':
        char()
    elif menu=='d':
        words()
    elif menu=='e':
        search=input('enter word to search:')
        print('The given word is  ',ser(search),'  times')