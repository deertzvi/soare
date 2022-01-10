import time
from collections import defaultdict

solutionsList = open("solutionList.txt","r")
solutions = solutionsList.read().split(',')
solutionsList.close()

# herringsList=open("herringList.txt","r")
# herrings=herringsList.read().split(',')
# herringsList.close()     

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#%%%%% prompts
def mainPrompt():
    """Prints main menu options and takes user input
    """
    global mainChoice
    global killSwitch
    if killSwitch=='Q':
        return
    else:
        print('\n')
        print('Main Menu:')
        print('[1] Information about overall frequency of letters')
        print('[2] Information about frequency of letters in each position within solution words')
        print('[3] Try a new set of letters')
        print('[Q] Quit')
        print('Your current test letters are',testLetters)
        time.sleep(1)
        currChoice=input("What would you like to do? \n")
        currChoice=currChoice.strip(' ').upper()
        killSwitch=currChoice
        mainChoice=currChoice   
    return 

def listPrompt():
    """Prints menu options for wordlists including/excluding letters and takes user input
    """
    global listChoice
    global killSwitch
    print('\n')
    print('Overall Frequency:')
    print('[1] Find words which contain at least some minimum number of test letters')
    print('[2] Find words which contain fewer than some maximum number of test letters')
    print('[3] Return to the main menu')
    print('[Q] Quit')
    time.sleep(1)
    currChoice=input("What would you like to do? \n")
    currChoice=currChoice.strip(' ').upper()
    killSwitch=currChoice
    listChoice=currChoice
    return

def posPrompt():
    """Prints menu options for position information
    """
    global posChoice
    global killSwitch
    print('\n')
    print('Frequency by Position:')
    print('[1] For each position (1 throught 5), sort letters in descending order by frequency')
    print('[2] For each test letter, sort positions (1 through 5) in descending order by frequency')
    print('[3] Return to the main menu')
    print('[Q] Quit')
    time.sleep(1)
    currChoice=input("What would you like to do? \n")
    currChoice=currChoice.strip(' ').upper()
    killSwitch=currChoice
    posChoice=currChoice
    return
#%%%%% function definitions for wordlist and position operations
def newLetters():
    global presentDict
    global absentList
    global presentList
    global testLetters
    
    presentDict=defaultdict(list)
    absentList=list()
    presentList=list()
    
    letterSet = [str(x) for x in input("Enter test letters, separated by commas: ").split(",")]
    x=0
    for item in letterSet:
        letterSet[x]=item.strip(' ').lower()
        x=x+1
    testLetters=letterSet
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
    return

def listMin():
    global minList
    minList=[]
    minNum=input('Enter a number (1-5) to find out how many possible solutions have at least that many spaces filled by test letters:\n')
    for key,value in presentDict.items():
        if int(key)>=int(minNum):
            minList=[*minList,*value]
    minCount=len(minList)
    print('\n')
    print('Test letters:',testLetters)
    print('Words with at least',minNum,'character(s) matching a test letter:\n',minCount,'out of',len(solutions))
    time.sleep(1)
    print('\n')
    seeList=int(input('Would you like to see the list?\n[1] Yes \n[2] No\n'))
    if seeList==1:
        print('\n')
        print(minList)
    time.sleep(1)
    return
        
def listMax():
    global maxList
    maxList=absentList
    maxNum=int(input('Enter a number (1-5) to find out how many possible solutions have fewer than that many spaces filled by test letters:\n'))
    for key,value in presentDict.items():
        if int(key)<maxNum:
            maxList=[*maxList,*value]
    maxCount=len(maxList)
    uncommonCount={
    }
    for a in alphabet:#for each letter
        u=0 #start a new counter
        for x in maxList:#for every word in the new list
          for y in range(5): #for every letter in the word
            if x[y]==a: #if it matches the current letter
                u=u+1 #increase the letter count by one
        uncommonCount[a]=u
    maxDict=dict()
    maxlistFreq=sorted(uncommonCount.items(), key=lambda x: x[1], reverse=True)
    for y in range(9):
        lett=maxlistFreq[y][0]
        maxDict[lett]=maxlistFreq[y][1]
    print('\n')
    print('Test letters:',testLetters)
    print('Words with fewer than',maxNum,'character(s) matching a test letter:\n',maxCount,'out of',len(solutions))
    print('Ten most common letters in this wordlist (in descending order of frequency):',maxDict)
    print('\n')
    
    time.sleep(1)
    print('\n')
    seeList=int(input('Would you like to see the list?\n[1] Yes \n[2] No\n'))
    if seeList==1:
        print('\n')
        print(maxList)
    time.sleep(1)
    return

def byPos():
    print('\n')
    perPos=dict()
    for y in range(5):
        for z in testLetters:
            w=0
            for x in solutions:
                if str(x)[y]==str(z):
                    w=w+1
            zUpper=z.upper()
            perPos[zUpper]=w
        posList=sorted(perPos.items(), key= lambda x: x[1], reverse=True )
        print('Position',y+1)
        for (i,j) in enumerate(posList):
            print(j[0],':',j[1])
        print('\n')
        time.sleep(1)
    return

def byLet():
    print('\n')
    perLet=dict()
    for z in testLetters:
        for y in range(5):  
            pos=y+1
            w=0
            for x in solutions:
                if str(x)[y]==str(z):
                    w=w+1
            perLet[pos]=w
        letList=sorted(perLet.items(), key= lambda x: x[1], reverse=True )
        zUpper=z.upper()
        print('Occurrences of',zUpper)
        for (i,j) in enumerate(letList):
            print(j[0],':',j[1])
        print('\n')
        time.sleep(1)
    return

#%%%%% definitions for option menus 

def listMenu():
    global killSwitch
    while killSwitch != 'Q':
        listPrompt()
        if listChoice=='1':
            listMin()
        if listChoice=='2':
            listMax()
        if listChoice=='3':
            return 
        if listChoice=='Q':
            killSwitch='Q'
            return
    return
    return
def posMenu():
    global killSwitch
    while killSwitch != 'Q':
        posPrompt()
        if posChoice=='1':
            byPos()
        if posChoice=='2':
            byLet()
        if posChoice=='3':
            return
        if posChoice=='Q':
            killSwitch='Q'
            return

    return

#%%
killSwitch='A' 
mainChoice='A'
newLetters()
while killSwitch != 'Q':
    if mainChoice=='1':
        listMenu()
    elif mainChoice=='2':
        posMenu()
    elif mainChoice=='3':
        newLetters()
    mainPrompt()
print('Bye for now!')
