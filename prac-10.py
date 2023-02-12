f=open('simpletext.txt','r')
fr=f.read()
vowels=0
consonants=0
upcase=0
lowcase=0
for i in fr:
    if i.isalpha():
        if i.isupper():
            upcase+=1
        elif i.islower():
            lowcase+=1
        if i in 'aeiouAEIOU':
            vowels+=1
        else:
            consonants+=1
print('vowels:',vowels,'\nconsonants:',consonants,'\nuppercase characters:',upcase,'\nlowercase characters:',lowcase)
f.close()