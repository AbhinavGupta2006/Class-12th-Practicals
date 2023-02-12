def listSearch(Thelist,element):
    def lElement(element):
        frequency=Thelist.count(element)
        print('Frequency of',element,'in list is:',frequency)
        print('locations of',element,':',end='')
        for i in range(len(Thelist)):
            if Thelist[i]==element:
                print(i)
    return lElement(element)
asklist=eval(input('Enter the list: '))
elmnt=int(input('Enter the element name to search for:'))
print(listSearch(asklist,elmnt))