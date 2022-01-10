# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 20:04:28 2022

@author: tzvin
"""
import time
from collections import defaultdict
#%%import solutions
solutionsList = open("solutionList.txt","r")
solutions = solutionsList.read().split(',')
solutionsList.close()
# #%%import herrings  
# herringsList=open("herringList.txt","r")
# herrings=herringsList.read().split(',')
# herringsList.close()     
#%% define variables
#alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#%%function definitions
def posPrompt():
    """
    Prints list of position choices (main menu>choice 2).
    """
    print('\n')
    print('[1] Find test letter frequency for each position in a 5-letter word')
    print('[2] Find most common position in solution words for each test letter')
    print('[Q] Return to the previous screen')
def excluPrompt():
    """
    Prints list of wordlist choices (main menu>choice 1).
    """
    print('\n')
    print('[1] Find words which have at or over some minimum number of test letters')
    print('[2] Find words which have fewer than some maximum number of test letters')
    print('[Q] Return to the previous screen')
def mainPrompt():
    """
    Prints list of main menu choices.
    """
    print('\n')
    print('[1] Find possible solutions excluding/including some number of test letters')
    print('[2] Find information about which position in a word tends to be occupied by which test letter')
    print('[Q] Return to the previous screen')
def newLetters():
    global presentDict 
    presentDict=defaultdict(list)
    global absentList
    absentList=list()
    global presentList
    presentList=list()
    global testLetters
    testLetters = [str(x) for x in input("Enter test letters, separated by commas: ").split(",")]
    x=0
    for item in testLetters:  
       testLetters[x]=item.strip(' ').lower()
       x=x+1
       #make a list of words with at least one test letter and a list with no test letters
    for i in range(6):
        presentDict[i]=list()
    for x in solutions:
        c=0
        for y in range(5):
            for z in testLetters:
                if x[y]==z:
                    c=c+1
        if c==0: 
            absentList.append(x)
        else: 
            presentDict[c].append(x)
            presentList.append(x)

def wordsMin():
    minNum=int(input('Enter a number (1-5) to find out how many possible solutions have at least that many spaces filled by test letters:\n'))
    minCount=0
    for key,value in newLetters()[0].items():
        if int(key)>=minNum:
            minCount=minCount+len(value)
    print('\nWords with at least',minNum,'character(s) matching a test letter:\n',minCount,' out of ',len(solutions),'\n')
    time.sleep(1)
def wordsMax():
    maxNum=int(input('Enter a number (1-5) to find out how many possible solutions have fewer than that many spaces filled by test letters:\n'))
    maxCount=len(newLetters()[2])
    for key,value in newLetters()[0].items():
        if int(key)<maxNum:
            maxCount=maxCount+len(value)
    print('\nWords with fewer than',maxNum,'character(s) matching a test letter:\n',maxCount,' out of ',len(solutions),'\n')
    time.sleep(1)
def excludedWords():
    excluPrompt()
    numChoice=input("What would you like to do?\n")
    numChoice=numChoice.strip(' ').upper()
    while numChoice != 'Q':
        if numChoice=='1':
            wordsMin()
            time.sleep(1)   
        elif numChoice=='2':
            wordsMax()
            time.sleep(1)     
        excluPrompt()
        numChoice= input("What would you like to do?\n")
        numChoice=numChoice.strip(' ').upper()
#%%
def letPerPos(posList):
    posList=[]
    perPos=dict()
    print('\n')
    for y in range(5):
        for z in testLetters:
            w=0
            for x in solutions:
                if str(x)[y]==str(z):
                    w=w+1
            zUpper=z.upper()
            perPos[zUpper]=w
        posList.append(sorted(perPos.items(), key=lambda x: x[1], reverse=True)) 
        print('Position',y+1)
        for i in posList[y]:
             print(i[0],':', i[1])
        print('\n')     
    time.sleep(1)
    return posList
def posPerLet(letList):
    perLet=dict()
    print('\n')
    for z in testLetters:
        letList=[]
        for y in range(5):
            pos=(y+1)
            c=0
            # numDict={
            #     }
            for x in solutions:
                if str(x)[y]==z:
                    c=c+1
            perLet[pos]=c
        letList=sorted(perLet.items(),key=lambda x:x[1], reverse=True)
        print('Occurrences of',z.upper(),':')
        for (i,j) in enumerate(letList):
            print('Position',j[0],':',j[1])
    time.sleep(1)                  
def getPos():
    posPrompt()
    posChoice=input("What would you like to do?\n")
    posChoice=posChoice.strip(' ').upper()
    while posChoice!='Q':
        if posChoice=='1':
            letPerPos(posList)
            time.sleep(1)
        elif posChoice=='2':
            posPerLet(letList)
            time.sleep(1)
        posPrompt()
        posChoice=input("What would you like to do?\n")
        posChoice=posChoice.strip(' ').upper()        
#%%
choice=''
newLetters()
while choice != 'X':
    if choice=='Q':
        newLetters()
    if choice=='1':
        excludedWords()
    elif choice =='2':
        getPos()
    mainPrompt()
    choice = input("What would you like to do? ")
    choice=choice.strip(' ').upper()
print('Bye for now!')    