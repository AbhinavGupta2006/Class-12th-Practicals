def countVowels():
    c=0
    f=open('textfilewithvowel.txt','r')
    fr=f.read()
    for i in fr:
        if i.lower() in 'aeiou':
            c+=1
    f.close()
    return c
print(countVowels(), 'vowels')

'''if the question had been to write a function to count given string in text file'''

def findstr(thestring):
    c=0
    f=open('textfilewithvowel.txt','r')
    fr=f.readlines()
    for i in fr:
        if thestring in i:
            c+=1
    f.close()
    return c
print(findstr(input('Enter the string to search: ')), 'times')