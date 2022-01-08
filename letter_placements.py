# -*- coding: utf-8 -*-
"""
load in the prerequisite info
"""
#%%
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#%%import the list of solutions
solutionsList = open("solutionList.txt","r")
solutions = solutionsList.read().split(', ')
solutionsList.close()
#%%import the herrings list
herringsList=open("herringList.txt","r")
herrings=herringsList.read().split(',')
herringsList.close()
#%%add the letters to test
commonLetters = [str(x) for x in input("Enter test letters, separated by commas: ").split(",")] 
#%%fix entries with spaces or caps
x=0
for item in commonLetters:  
    commonLetters[x]=item.strip(' ').lower()
    x=x+1
#%%find most common positions for each letter
############
numWords={
    }
print('\nMost frequently found in:\n')
for z in commonLetters:
    testLetter=z
    w=0 #start a counter
    for x in solutions: #for every word in the solution list
        testWord=str(x)
        if testWord.find(testLetter) != -1:#if the letter is in that word
            w=w+1 #increment the counter
    numWords[z]=w #save the final count
#####
    testDict={
        }
    for y in range(5):
        wordPos=y+1
        c=0
        for x in solutions:
            solLetter=x[y]
            if solLetter==testLetter: c=c+1
            pos="% s" %wordPos
            dval=('position '+str(pos))
        testDict[dval]=c
    max_key = max(testDict, key=testDict.get)
    print(testLetter.upper(),':',max_key)    
    for key, value in testDict.items():
        print(key,':',value)
    print(testLetter.upper(),'is in',numWords[z],'of',len(solutions),'possible solutions\n')    